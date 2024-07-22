from . import converter
import json

def handle_soap_request(handler):
    contentLength = int(handler.headers['Content-Length']) 
    soap_data = handler.rfile.read(contentLength)
    parsed_data = converter.parseSOAP(soap_data)
    
    # extract logic
    
    # send to respective api gateway to handle request
    
    # receive api response
    
    # parse back to JSON
    
    # send response
    handler.send_response(200)
    handler.send_header('Content-type', 'text/xml')
    handler.end_headers()
    
    handler.wfile.write(json.dumps(parsed_data).encode('utf-8'))
    return