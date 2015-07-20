from __future__ import unicode_literals

from drf2.views import APIView
from drf2 import authentication
from drf2 import renderers
from drf2.response import Response


class MockView(APIView):

    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = (renderers.BrowsableAPIRenderer,)

    def get(self, request):
        return Response({'a': 1, 'b': 2, 'c': 3})
