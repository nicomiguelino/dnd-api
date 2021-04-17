from functools import partial
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response


class APIRootView(APIView):
    def get(self, request, format=None):
        get_url = partial(reverse, request=request, format=format)

        return Response({
            'docs': {
                'redoc': get_url('redoc-docs'),
                'swagger': get_url('swagger-docs')
            },
            'characters': get_url('characters:list')
        })
