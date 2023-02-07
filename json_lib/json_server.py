from http.server import BaseHTTPRequestHandler, HTTPServer
from jsonrpcserver import method, Result, Success, dispatch


@method
def ping() -> Result:
    return Success("pong")


class TestHttpServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Main page")
        
        
    def do_POST(self):
        # Process request
        request = self.rfile.read(int(self.headers["Content-Length"])).decode()
        response = dispatch(request)
        # Return response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode())


if __name__ == "__main__":
    HTTPServer(("localhost", 5000), TestHttpServer).serve_forever()
