from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Movie_Model
from django.views.decorators.csrf import csrf_exempt
from Clients.models import ClientData, Clients
import json

@csrf_exempt
def get_movie(request, id):
    try:
        client = Clients.objects.get(client_id=request.headers["Clientid"])
        if client.key == request.headers["Key"]:
            try:
                clientdata = ClientData.objects.get(client_id= client.client_id)
                mapping = clientdata.data
                print(mapping)
                print(type(mapping))
                print(mapping.keys())
                movie = Movie_Model.objects.get(id=id)

                data_all = {
                    'title' : movie.title,
                    'release_date' : movie.release_date,
                    'description' : movie.description,
                    'director' : movie.director,
                    'actors' : movie.actors,
                    'genre' : movie.genre,
                    'rating' : movie.rating,
                    'runtime' : movie.runtime,
                    'id': movie.id
                }

                data = {}
                for key in mapping.keys():
                    data[mapping[key]] = data_all[key]

                js_data = json.dumps(data)
                return HttpResponse(js_data, content_type='application/json')
            except Movie_Model.DoesNotExist:
                return HttpResponse(json.dumps({'error': 'Movie ID does not exist'}), content_type='application/json')

        else:
            return HttpResponse(json.dumps({'error': 'Wrong Key'}), content_type='application/json')
    except Clients.DoesNotExist:
        return HttpResponse(json.dumps({'error': 'Client Not Authorized'}), content_type='application/json')
