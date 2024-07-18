# driver code which handles server instrument

from http.server import BaseHTTPRequestHandler, HTTPServer

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
            path = self.path
            message = "Hello, world!"

            if path == '/rs':
                # rest to soap handler here
                message = "converting rest to soap"
            elif path == '/sr':
                # soap to rest handler here
                message = "converting soap to rest"

            # Response status code
            self.send_response(200)

            # Add headers to response
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # HTML content to send
            
            
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            return



def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
     run(handler_class= requestHandler)