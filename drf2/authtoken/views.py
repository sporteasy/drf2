from drf2.views import APIView
from drf2 import status
from drf2 import parsers
from drf2 import renderers
from drf2.response import Response
from drf2.authtoken.models import Token
from drf2.authtoken.serializers import AuthTokenSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_auth_token = ObtainAuthToken.as_view()
