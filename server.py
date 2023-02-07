from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
from parser_json import ParsJson


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>hello !</h1>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        try:
            pars = ParsJson(json.loads(body))
            str_json = pars.pars_request.encode()
            response = BytesIO()
            response.write(str_json)
            self.wfile.write(response.getvalue())
        except ValueError:
            self.wfile.write(b"Error type of data. Input int or float!")


def run(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('', 5000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
