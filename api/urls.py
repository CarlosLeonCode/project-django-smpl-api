from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.movie_views import MovieViewSet
from api.views.rating_views import RatingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
