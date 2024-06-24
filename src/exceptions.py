class ApiException(Exception):
    status_code = 500
    title = "Server Error"
    message = "An unexpected error occurred"

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status'] = self.status_code
        rv['title'] = self.title
        rv['detail'] = self.message
        return rv
    
class InvalidAPIUsage(ApiException):
    status_code = 400
    title = "Invalid API Usage"

class JSONQueryInput(InvalidAPIUsage):
    title = "Input Query Not Valid"
    message = "Query parameters not in valid format"

class ResourceNotFound(ApiException):
    status_code = 404
    title = "Resource Not Found"

class CatalogNotFound(ResourceNotFound):
    title = "Catalog Not Found"
    message = "ID Catalog in not present in db"

class MethodNotAllowed(ApiException):
    status_code = 405
    title = "Methon Not Allowed"




