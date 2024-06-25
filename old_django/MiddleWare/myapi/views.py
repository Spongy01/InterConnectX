import json

# from django.contrib.sites import requests
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Protocol_Relation
from .helpers import dict_to_soap, xml_to_dict
import xmltodict

@csrf_exempt
def api_call(request):
    headers = request.headers
    client_id = headers["Clientid"]
    middleware_key = headers["Key"]
    print("Client ID is : "+ str(client_id))
    print("Middleware Key is : "+ middleware_key)
    try:
        client = Protocol_Relation.objects.get(caller_id=str(client_id))

        if client.middleware_key == middleware_key:
            # extract payload, user is authenticated

            payload = json.loads(request.body)
            print("Payload type is : " + str(type(payload)))
            print("Payload type is : " + str(payload))
            print('Service URL is : '+ payload["service_url"])
            server = Protocol_Relation.objects.get(caller_url=payload["service_url"])
            server_id = server.caller_id
            server_protocol = server.protocol
            print("Server_Protocol : "+ server_protocol)
            forw_header = {
                "Clientid": client_id, "Key": payload["service_key"]
            }
            # forw_payload = payload["payload"]
            if (server_protocol == 'REST'):
                print("We got Into REST")
                forw_header["content-type"] = "application/json"
                # payload = json.dumps(payload["payload"])
                response = requests.post(url=payload["service_url"]+payload["payload"]["id"], headers=forw_header,)
                print("Resposen : "+ response.text)
                resp = json.loads(response.text)
                print(type(resp))
                if request.headers['content-type'] == "application/json":

                    return HttpResponse(json.loads(response.text), content_type='application/json')
                if request.headers['content-type'] == "application/xml": # JSON to XML conversion
                    data = json.loads(response.text)
                    print("My data is :" + str(data))
                    return HttpResponse(dict_to_soap(data), content_type='application/xml')


            elif (server_protocol == 'SOAP'):
                print("We got Into Soap")
                forw_header["content-type"] = "application/xml"
                forw_payload = payload["payload"]
                print("Url link is : "+ payload["service_url"]+payload["payload"]['isbn'])
                response = requests.post(url=payload["service_url"]+payload["payload"]['isbn'], headers=forw_header)
                print("got response")
                print(response.text)
                if request.headers['content-type'] == "application/json": #  XML to JSON conversion
                    print("parsing")
                    dict_data = xmltodict.parse(response.text)
                    dict_data =  dict(dict_data)
                    print("Parsed Data is : "+ str(dict_data))
                    return HttpResponse(json.dumps(dict_data['soap:Envelope']["soap:Body"]))
                if request.headers['content-type'] == "application/xml":
                    return response


    except Protocol_Relation.DoesNotExist:
        return HttpResponse("Client is not Authenticated with the Middleware")

    return HttpResponse("IT RUNS VIOLA")
