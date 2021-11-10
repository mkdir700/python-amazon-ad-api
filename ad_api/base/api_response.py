import pprint

from requests import Response


class ApiResponse:
    def __init__(self, payload=None, nextToken=None, **kwargs):
        self.response: Response = kwargs.pop("response", None)
        self.payload = payload
        self.headers = kwargs
        self.next_token = self.set_next_token(nextToken)
    
    def __str__(self):
        return pprint.pformat(self.__dict__)
    
    def set_next_token(self, nextToken=None):
        if nextToken:
            return nextToken
        try:
            return self.payload.get('NextToken', None) or self.headers.get('NextToken', None)
        except AttributeError:
            return None
    
    @staticmethod
    def set_rate_limit(headers: dict = None):
        try:
            return headers['x-amzn-RateLimit-Limit']
        except (AttributeError, KeyError, TypeError):
            return None
    
    @property
    def reason(self):
        return self.response.reason
    
    @property
    def request(self):
        return self.response.request
