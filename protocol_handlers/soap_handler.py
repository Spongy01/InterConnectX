from . import converter
import json
import requests
import xmltodict

def handle_soap_request(request):
    if(request.headers['Content-Length'] is None):
        contentLength = 0
    else:
        contentLength = int(request.headers['Content-Length']) 
        
    soap_data = request.rfile.read(contentLength)
    parsed_data = ""
    if(request.headers['Content-Length'] is not None):
        print("Content Length : " + request.headers['Content-Length'])
        parsed_data = converter.parseSOAP(soap_data)
    
    # extract endpoint logic
    if request.headers['Endpoint']:
        print("Endpoint : " + request.headers['Endpoint'])
    else:
        print("Endpoint Not Provided")
        request.send_response(200)
        request.send_header('Content-type', 'text/xml')
        request.end_headers()
        
        request.wfile.write(b'Endpoint header not provided')
        return

    
    # send to respective api gateway to handle request and handle responses
    response = requests.get(url=request.headers['Endpoint'], data=parsed_data)
    print("RESPONSE : ", response.json())

    try:
        json_response = response.json()
        xml_response = xmltodict.unparse({"response": json_response}, pretty=True)
    except ValueError:
        xml_response = '<error>Invalid JSON response</error>'
    # parse back to JSON
    # soap_response = converter.convertJSONtoSOAP(json_response)
    print("SOAP response : " + xml_response)
    
    # send response
    request.send_response(response.status_code)
    
    request.send_header('Content-type', 'application/XML')
    request.end_headers()
    
    request.wfile.write(xml_response.encode('utf-8'))
    return