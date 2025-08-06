class Controller:
    def __init__(self):
        pass

    def handle_request(self, request):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def handle_response(self, response):
        raise NotImplementedError("Subclasses should implement this method.")