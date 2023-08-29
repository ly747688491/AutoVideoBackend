from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler
from rest_framework.response import Response
import rest_framework.status as status
import logging
logger = logging.getLogger('log')

# The `BaseResponse` class is a basic response object with properties for code, data, and message.
class BaseResponse(object):

    def __init__(self):
        self.code = 200
        self.data = None
        self.msg = None

    @property
    def dict(self):
        return self.__dict__


class FitJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        
        response_body = BaseResponse()
        response = renderer_context.get("response")
        response_body.code = response.status_code
        response_body.data = data  # data里是详细异常信息
        if response_body.code >= 400:  # 响应异常
            prefix = ""
            if isinstance(data, dict):
                prefix = list(data.keys())[0]
                data = data[prefix]
            if isinstance(data, list):
                data = data[0]
            response_body.msg = f"{prefix}:{str(data)}"
        renderer_context.get("response").status_code = 200  # 统一成200响应,用code区分
        return super(FitJSONRenderer, self).render(response_body.dict, accepted_media_type, renderer_context)
