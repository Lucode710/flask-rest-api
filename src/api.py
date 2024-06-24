from flask import Flask, jsonify, request
from .mock_database import MockDatabase
from .exceptions import *
from .validations import *

class Api(object):

    def __init__(self, app : Flask):
        self.app = app
        self.init_routes(self.app)
        self.init_exceptions(self.app)
    
    def init_routes(self,app):

        @app.route('/api/catalogs/<int:catalog_id>/prizes', methods=['GET'])
        def list_prizes(catalog_id):

            validate_catalog_id(catalog_id)

            filter = request.args.get('filter')
            pagination = request.args.get('pagination')

            filter_dict = json_validation_input(filter)
            pagination_dict = json_validation_input(pagination)

            if(filter):
                validate_filter(filter_dict)
            
            if(pagination_dict):
                validate_pagination(pagination_dict)


            try:
                total, prizes = MockDatabase.get_prizes(catalog_id, filter=filter_dict, pagination=pagination_dict)
                prizes_list = [{
                    'id': prize.id,
                    'title': prize.title,
                    'description': prize.description,
                    'image': prize.image
                } for prize in prizes]

                return jsonify({'total': total, 'prizes': prizes_list})
            
            except ValueError as e:
                return InvalidAPIUsage(str(e))
    
    def init_exceptions(self, app):

        @app.errorhandler(ApiException)
        def invalid_api_usage(e):
            return jsonify(e.to_dict()), e.status_code

        @app.errorhandler(404)
        def handle_404(e):
            return invalid_api_usage(ResourceNotFound(str(e)))
        
        @app.errorhandler(405)
        def handle_405(e):
            return invalid_api_usage(MethodNotAllowed(str(e)))