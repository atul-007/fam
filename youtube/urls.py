from django.urls import path
from . import views

urlpatterns = [
    path('getVideos/', views.ListVideos.as_view(), name='get-videos'),
    path('searchVideos/', views.ListVideoSearch.as_view(), name='get-videos-by-search'),
    path('addAuthKey/', views.AddAuthKey.as_view(), name='add-auth-key'),
]
