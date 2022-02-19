from datetime import datetime


class CustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.current_time = datetime.now()
        print("From middle ware request", request)
        response = self.get_response(request)
        return response
