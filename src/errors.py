from werkzeug.exceptions import HTTPException


class ParameterMissing(HTTPException):
    pass


class InvalidAnswersFormat(HTTPException):
    pass


class MidtermSubmissionExpiration(HTTPException):
    pass


class InvalidMidtermMember(HTTPException):
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
    "InvalidAnswersFormat": {
        "message": "Answers format is invalid",
        "code": "invalid_answers",
        "status": 400,
    },
    "MidtermSubmissionExpiration": {
        "message": "Time for midterm submission is expired",
        "code": "midterm_submission_expiration",
        "status": 403,
    },
    "InvalidMidtermMember": {
        "message": "Invalid sid or credential for midterm member",
        "code": "invalid_midterm_member",
        "status": 403,
    },
}
