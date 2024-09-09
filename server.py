# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the entire request
        print(f"Received request: {self.requestline}")
        print(f"Headers:\n{self.headers}")
        
        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hi')

    def do_POST(self):
        # Print the entire request
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length)  # Read the posted data
       
        print("running curl")

        # URL for the API endpoint
        url = "http://localhost:8153/go/api/admin/materials/git/notify"

        # Headers for the request
        headers = {
            "Accept": "application/vnd.go.cd.v2+json",
            "Content-Type": "application/json"
        }

        # Data to be sent in the request body
        data = {
            "repository_url": "https://github.com/oscols/DD2482-Demo.git"
        }

        # Make the POST request
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        print("done")

        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'POST received')


def run(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()