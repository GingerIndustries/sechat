class SEChatException(Exception):
    pass


class FutureError(SEChatException):
    """Used for errors that occur due to a required service drastically changing sometime in the future"""

    pass


class LoginError(SEChatException):
    """Used for errors caused due to login failure"""

    pass


class RoomError(SEChatException):
    """Errors relating to rooms"""

    pass


class ConnectionError(RoomError):
    """Used for room connection errors"""

    pass


class RatelimitError(RoomError):
    """Used when ratelimiting is triggered"""

    def __init__(self, retryAfter: int):
        super().__init__()
        self.retryAfter = retryAfter


class NotAllowedError(RoomError):
    """Used when you try to do something you're not allowed to do"""


class OperationFailedError(RoomError):
    """Used when an operation fails"""
