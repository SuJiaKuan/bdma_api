from werkzeug.exceptions import HTTPException


class ParameterMissing(HTTPException):
    pass


errors = {
    "EndpointNotFound": {
        "message": "Endpoint is not found",
        "code": "endpoint_not_found",
        "status": 404,
    },
    "MethodNotAllowed": {
        "message": "The method is not allowed for the requested URL",
        "code": "method_not_allowed",
        "status": 405,
    },
    "ServerError": {
        "message": "The server has encountered a situation it doesn\"t know "
                   "how to handle",
        "code": "server_error",
        "status": 500,
    },
    "ParameterMissing": {
        "message": "One or more required values are missing",
        "code": "parameter_missing",
        "status": 400,
    },
}
