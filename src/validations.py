from src.exceptions import *
import json

def json_validation_input(input :str):
    try:
        return json.loads(input) if input else {}
    except json.JSONDecodeError:
        raise JSONQueryInput()
    
def validate_catalog_id(catalog_id):
    if not isinstance(catalog_id, int) or catalog_id <= 0:
        raise InvalidAPIUsage("Invalid catalog_id. Must be a positive integer.")

def validate_filter(filter_dict):
    if not isinstance(filter_dict, dict):
        raise InvalidAPIUsage("Invalid filter. Must be a dictionary.")
    if not 'id' in filter_dict and not 'description' in filter_dict:
        raise InvalidAPIUsage("Invalid key to filter")
    if 'id' in filter_dict and (not isinstance(filter_dict['id'], int) or filter_dict['id'] <= 0):
        raise InvalidAPIUsage("Invalid id in filter. Must be a positive integer.")
    if 'description' in filter_dict and not isinstance(filter_dict['description'], str):
        raise InvalidAPIUsage("Invalid description in filter. Must be a string.")

def validate_pagination(pagination_dict):
    if not isinstance(pagination_dict, dict):
        raise InvalidAPIUsage("Invalid pagination. Must be a dictionary.")
    if not ('page' in pagination_dict and 'per_page' in pagination_dict):
        raise InvalidAPIUsage("A required key for pagination. Must have 'page' and 'per_page' key")
    if 'page' in pagination_dict and (not isinstance(pagination_dict['page'], int) or pagination_dict['page'] <= 0):
        raise InvalidAPIUsage("Invalid page in pagination. Must be a positive integer.")
    if 'per_page' in pagination_dict and (not isinstance(pagination_dict['per_page'], int) or pagination_dict['per_page'] <= 0):
        raise InvalidAPIUsage("Invalid per_page in pagination. Must be a positive integer.")