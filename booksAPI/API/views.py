from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Book_Model
from django.http import JsonResponse
from .helpers import dict_to_soap
import json
from Clients.models import ClientData, Clients


@csrf_exempt
def get_book(request, isbn):
    print("Headers Received are : "+ str(request.headers))
    # payload = json.load(request.text)
    # isbn = payload["isbn"]
    try:
        client = Clients.objects.get(client_id=request.headers["Clientid"])
        if client.key == request.headers["Key"]:
            try:
                clientdata = ClientData.objects.get(client_id= client.client_id)
                mapping = clientdata.data
                print(mapping)
                print(type(mapping))
                print(mapping.keys())
                book = Book_Model.objects.get(isbn=isbn)

                data_all = {
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'publisher': book.publisher,
                    'publication_date': str(book.publication_date),
                    'description': book.description,
                    'language': [book.language],
                    'price': str(book.price),
                    'avg_rating': str(book.average_rating),
                }
                data={}
                for key in mapping.keys():
                    data[mapping[key]] = data_all[key]

                # print(dict_to_soap(data))
                return HttpResponse(dict_to_soap(data), content_type='application/xml')

            except Book_Model.DoesNotExist:
                return JsonResponse({'error': 'Book not found.'}, status=404)

        else:
            return HttpResponse(dict_to_soap({'error': 'Wrong Key'}),  content_type='application/xml')
    except Clients.DoesNotExist:
        return HttpResponse(dict_to_soap({'error': 'Client Not Authorized'}), content_type='application/xml')


