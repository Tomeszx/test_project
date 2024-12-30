import inspect
import os
import sys


sys.tracebacklimit = 0


class BaseError(Exception):
    def __init__(self, *messages: str):
        stack = inspect.stack()
        stack_info = ''
        for code_frame in stack[2:4]:
            file_path = os.path.abspath(code_frame.filename)
            line_number = code_frame.lineno
            function_name = code_frame.function
            code = " ".join(code_frame.code_context).strip().replace("\n", "")
            stack_info += f'\n  File "{file_path}", line {line_number}, in {function_name}\n    {code}'
        full_msg = self._convert_error_msgs(messages)
        super().__init__(f'{full_msg}')

    @classmethod
    def _convert_error_msgs(cls, messages: tuple[str, ...]) -> str:
        full_msg = ""
        msg_indent = 6
        for message in messages:
            if message:
                full_msg += f'\n{" " * msg_indent}{message}'
                msg_indent += 2
        return full_msg
