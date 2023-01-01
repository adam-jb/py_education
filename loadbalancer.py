
import socketserver
import requests

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        html_code = '<html><body>Hello World!</body></html>'
        
        # If you wanted to fwd the request to the endpoint
        #endpoint_url = "http://localhost:9900"
        #response = requests.get(endpoint_url)
        
        # Build the HTTP response
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(html_code)}\r\n\r\n{html_code}"
        print(f'response:\n{response}')

        # Send the HTTP response to the client
        self.request.sendall(response.encode())
        
class LoadBalancer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def process_request(self, request, client_address):
    #def process_request(self):
        print('hi')
        print(f'request: {request}')
        print(f'client_address: {client_address}')
        
        # this ensures MyHandler() is called, as MyHandler is the RequestHandlerClass of this class
        self.RequestHandlerClass(request, client_address, self)
        
if __name__ == "__main__":
    # Create a load balancer server
    server = LoadBalancer(("0.0.0.0", 8080), MyHandler)
    # Start the server
    server.serve_forever()

    
    


