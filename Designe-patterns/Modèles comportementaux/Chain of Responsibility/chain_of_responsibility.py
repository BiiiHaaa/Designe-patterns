class Handler:
    """Abstract handler class"""
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return None

class LowLevelHandler(Handler):
    """Handles low-level requests"""
    def handle_request(self, request):
        if request < 10:
            return f"LowLevelHandler processed request {request}"
        return super().handle_request(request)

class MidLevelHandler(Handler):
    """Handles mid-level requests"""
    def handle_request(self, request):
        if 10 <= request < 50:
            return f"MidLevelHandler processed request {request}"
        return super().handle_request(request)

class HighLevelHandler(Handler):
    """Handles high-level requests"""
    def handle_request(self, request):
        if request >= 50:
            return f"HighLevelHandler processed request {request}"
        return super().handle_request(request)

# Setting up the chain
handler_chain = LowLevelHandler(MidLevelHandler(HighLevelHandler()))

# Test requests
requests = [5, 20, 100]

for req in requests:
    print(handler_chain.handle_request(req))
