"""
HTTP exceptions from the application
We could override the get_body and get_headers base functions but that would be a lot of work
"""

from werkzeug.exceptions import BadRequest, Conflict, NotFound, Unauthorized


class ValidationError(BadRequest):
    name = 'ValidationError'

    def __init__(self, messages, response=None):
        super().__init__(messages, response)


class UserAlreadyExist(Conflict):
    name = 'UserAlreadyExists'

    def __init__(self, email_address, response=None):
        super().__init__(f"The email address '{email_address}' is no longer available.", response)


class UserNotFound(NotFound):
    name = 'UserNotFound'

    def __init__(self, email_address, response=None):
        super().__init__(f"User with email address '{email_address}' was not found.", response)


class IncorrectUserPassword(Unauthorized):
    name = 'IncorrectUserPassword'

    def __init__(self, response=None):
        super().__init__(f"Password submitted is incorrect.", response)


class NoteNotFound(NotFound):
    name = 'NoteNotFound'

    def __init__(self,note_id, response=None):
        super().__init__(f"Note with noteId '{note_id}' was not found.", response)