from rest_framework import viewsets

from .models import (
    Fish,
)
from .serializers import (
    FishSerializer,
)


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.order_by('created_at').all()
    serializer_class = FishSerializer

    # def get_queryset(self):
    #     queryset = Fish.objects.filter(pk=self.kwargs['post_id'])
    #     return queryset