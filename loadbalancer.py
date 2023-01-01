import socketserver
import threading

class LoadBalancer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Override the process_request method to distribute incoming requests to a pool of worker threads
    def process_request(self, request, client_address):
        print('hi')
        print(f'request: {request}')
        print(f'client_address: {client_address}')
        return 'hahaha'
        """
        # Create a new worker thread to handle the request
        t = threading.Thread(target=self.process_request_thread, args=(request, client_address))
        # Start the worker thread
        t.start()
        """
if __name__ == "__main__":
    # Create a load balancer server
    server = LoadBalancer(("0.0.0.0", 8080), socketserver.BaseRequestHandler)
    # Start the server
    server.serve_forever()
