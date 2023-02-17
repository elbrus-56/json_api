import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from parser_json import ParsJson


class HttpProcessor(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        if self.path == '/api/v1/':
            
            try:
                # Reading the file
                with open('api/v1/data.json', "r+") as fp:
                    file_to_open = json.load(fp)
                    fp.truncate(0)
                
                self.send_response(200)
                self.send_header("Content-type", "application/json")
            except:
                file_to_open = "Make a new request and refresh the pages"
                self.send_response(404)
            
            self.end_headers()
            self.wfile.write(bytes(str(file_to_open), 'utf-8'))
        
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<a href="http://127.0.0.1:5000/api/v1/">Link to json file</a>')
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode()
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        try:
            pars = ParsJson(json.loads(body))
            pars.generate_link()
            str_json = pars.json_response.encode()
            response = BytesIO()
            response.write(str_json)
            self.wfile.write(response.getvalue())
        
        except ValueError:
            self.wfile.write(b"Wrong value")
        except TypeError:
            self.wfile.write(b"Wrong type of data")
        except KeyError:
            self.wfile.write(b"Error key")
        except NameError:
            self.wfile.write(b"Error name of method")


def run(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('', 5000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
