# driver code which handles server instrument

from http.server import BaseHTTPRequestHandler, HTTPServer
from lxml import etree
from protocol_handlers import soap_handler

class requestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
            path = self.path
            
            if path == '/rs':

                message = "converting rest to soap"
            elif path == '/sr':

                soap_handler.handle_soap_request(self)
                         
            else:
             
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                
                self.wfile.write(b'Default Receiver')
                return

                
            



def run(server_class=HTTPServer, handler_class=requestHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
     run(handler_class= requestHandler)