from typing import Optional, List


class CalculatedError(Exception):
    status_code: int
    message: str

    def __init__(self, status_code: Optional[int] = None, message: Optional[str] = None):
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message

    def to_dict(self):
        return {
            "message": self.message
        }


class UserHasNoReplays(CalculatedError):
    status_code = 404
    message = "This user has no replays."


class ReplayNotFound(CalculatedError):
    status_code = 404
    message = "Replay not found."


class ErrorOpeningGame(CalculatedError):
    status_code = 500

    def __init__(self, error: str):
        message = f'Error opening game: {error}'
        super().__init__(self.status_code, message)


class PlayerNotFound(CalculatedError):
    status_code = 404
    message = "Player not found"


class MissingQueryParams(CalculatedError):
    status_code = 400

    def __init__(self, missing_params: List[str]):
        conditional_s = "" if len(missing_params) == 1 else "s"
        joined_missing_params = " and ".join(missing_params)
        message = f'Query parameter{conditional_s} {joined_missing_params} are required.'
        super().__init__(self.status_code, message)


class MismatchedQueryParams(CalculatedError):
    status_code = 400

    def __init__(self, query1: str, query2: str, list_size1, list_size2: int):
        message = f'Query parameter {query1} does not have the same number of elements as {query2}: '
        message += f'{list_size1} != {list_size2}'
        super().__init__(self.status_code, message)


class InvalidQueryParamFormat(CalculatedError):
    status_code = 400

    def __init__(self, invalid_parameter, value):
        message = f'[{value}] is in invalid format for Query parameter [{invalid_parameter.name}]'
        if invalid_parameter.tip is not None:
            message += f' tip: {invalid_parameter.tip}'
        super().__init__(self.status_code, message)


class TagNotFound(CalculatedError):
    status_code = 404
    message = "Tag not found"


class UnsupportedPlaylist(CalculatedError):
    status_code = 501
    message = "Playlist not supported"


class AuthorizationException(CalculatedError):
    status_code = 401
    message = "User not allowed for this request"
