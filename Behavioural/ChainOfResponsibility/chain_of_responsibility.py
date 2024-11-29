from abc import ABC, abstractmethod


# Handler Interface
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request: str):
        pass


# Concrete Handlers
class InfoHandler(Handler):
    def handle_request(self, request: str):
        if "INFO" in request:
            print(f"InfoHandler: Handling request '{request}'")
        elif self._next_handler:
            self._next_handler.handle_request(request)


class WarningHandler(Handler):
    def handle_request(self, request: str):
        if "WARNING" in request:
            print(f"WarningHandler: Handling request '{request}'")
        elif self._next_handler:
            self._next_handler.handle_request(request)


class ErrorHandler(Handler):
    def handle_request(self, request: str):
        if "ERROR" in request:
            print(f"ErrorHandler: Handling request '{request}'")
        elif self._next_handler:
            self._next_handler.handle_request(request)


# Client Code
if __name__ == "__main__":
    # Creating handlers
    info_handler = InfoHandler()
    warning_handler = WarningHandler()
    error_handler = ErrorHandler()

    # Setting up the chain of responsibility
    info_handler.set_next(warning_handler).set_next(error_handler)

    # Making requests
    print("Processing 'INFO' request:")
    info_handler.handle_request("INFO: Information message")

    print("\nProcessing 'WARNING' request:")
    info_handler.handle_request("WARNING: Warning message")

    print("\nProcessing 'ERROR' request:")
    info_handler.handle_request("ERROR: Error message")

    print("\nProcessing 'DEBUG' request:")
    info_handler.handle_request("DEBUG: Debugging message")
