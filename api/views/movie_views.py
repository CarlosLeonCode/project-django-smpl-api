from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.movie import Movie
from api.serializers.movie_serializer import MovieSerializer
from api.services.save_movie_from_omdb_service import SaveMovieFromOmdbService

class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

  def list(self, request):
    name = request.query_params.get('name', None)
    if name:
      queryset = Movie.objects.filter(title__icontains=name)
      if queryset.exists():
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
      else:
        service = SaveMovieFromOmdbService()
        return Response(service.exec(name))
    else:
      return Response({'error': 'Please provide a movie name as query parameter "name".'}, status=400)
