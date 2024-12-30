class BaseError(Exception):
    def __init__(self, *messages: str):
        full_msg = self._convert_error_msgs(messages)
        super().__init__(full_msg)

    @classmethod
    def _convert_error_msgs(cls, messages: tuple[str, ...]) -> str:
        full_msg = ""
        msg_indent = 6
        for message in messages:
            if message:
                full_msg += f'\n{" " * msg_indent}{message}'
                msg_indent += 2
        return full_msg
