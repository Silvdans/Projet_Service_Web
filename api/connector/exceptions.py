from rest_framework.exceptions import APIException

class UserHasAlreadyVotedException(APIException):
    """Exception raised when the user provided has already voted"""
    status_code = 400
    default_detail = 'This user has already vote about this movie.'

class UserDoNotExist(APIException):
    """Exception raised when the user provided do not exist"""
    status_code = 404
    default_detail = 'This user do not exist.'