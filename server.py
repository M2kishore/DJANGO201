from http.server import HTTPServer, SimpleHTTPRequestHandler

from datetime import datetime

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        print(self.path)# this is the current path
        if self.path == "/hello":
            content = content = f"<h1>{datetime.now()}<h1>"
        else:
            content = "<h1>Error</h1>"
        self.wfile.write(content.encode())

address = "127.0.0.1"
port = 3000
server_address = (address,port)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()