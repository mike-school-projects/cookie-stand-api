from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import CookieStand
from .serializer import CookieStandSerializer
from .permissions import isOwnerOrReadOnly

class CookieStandList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer