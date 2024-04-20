from django.contrib.postgres.search import SearchVector, SearchQuery
from rest_framework import generics, status
from .serializers import VideoSerializer, APIAuthKeySerializer
from rest_framework.pagination import PageNumberPagination
from .models import Video, APIAuthKey
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_limit'


class ListVideos(generics.ListAPIView):
    """
    View for getting all the videos with pagination.
    We can pass the query param 'page_limit' to give page size,
    otherwise, it will take the default page size as 10.
    """
    queryset = Video.objects.order_by('-publish_datetime')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ListVideoSearch(generics.ListAPIView):
    """
    View for getting videos by search keyword.
    We can pass query param 'query' to search video. It will search in the title and description of the video.
    """
    serializer_class = VideoSerializer
    pagination_class = VideoPagination

    def get_queryset(self):
        search_text = self.request.query_params.get('query')
        if search_text:
            vector = SearchVector('title', 'description', config='english')
            query = SearchQuery(search_text)
            return Video.objects.annotate(search=vector).filter(search=query)
        return Video.objects.none()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AddAuthKey(generics.CreateAPIView):
    """
    View responsible for adding auth keys.
    """
    serializer_class = APIAuthKeySerializer
    queryset = APIAuthKey.objects.all()

    def create(self, request, *args, **kwargs):
        auth_key = request.data.get('auth_key')
        if not auth_key:
            return Response({'error': 'Auth key is missing. Please provide auth_key in header'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
