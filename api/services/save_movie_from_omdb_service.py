from api.models.rating import Rating
from api.serializers.movie_serializer import MovieSerializer
from api.libs.omdb_api_client import OMDbApiClient
from rest_framework import status

class SaveMovieFromOmdbService:
  omdb_client = OMDbApiClient()
  
  def exec(self, name):
    try:
      # Find out on OMDB
      movie_data = self.omdb_client.search_movie_by_name(name)
      if movie_data:
        ratings = movie_data.get("Ratings",[])
        movie_data.pop("Ratings")
        
        # keys to lowercase and "N/A" values to None
        movie_data = dict((key.lower(), (None if value == "N/A" else value)) for key, value in movie_data.items())
        serializer = MovieSerializer(data=movie_data)

        # Saving data
        if serializer.is_valid():
          serializer.save()
          if ratings:
            for rating in ratings:
              data = dict((key.lower(), value) for key, value in rating.items())
              data['movie_id'] = serializer.data["id"]
              Rating.objects.create(**data)
          # Response
          data_response = [
            ratings,
            serializer.data
          ]
          return data_response
        else:
          error_message = {'error': 'Error saving movie data.'}
          return error_message, status.HTTP_500_INTERNAL_SERVER_ERROR
      else:
        error_message = {'error': 'Movie not found in OMDb API.'}
        return error_message, status.HTTP_404_NOT_FOUND
    except ValueError as e:
      error_message = {'error': 'Process Error'}
      return error_message, status.HTTP_500_INTERNAL_SERVER_ERROR
