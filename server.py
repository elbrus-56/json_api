import json
import logging.config
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from parser_json import ParsJson
from settings import logger_config

logging.config.dictConfig(logger_config)
server_logger = logging.getLogger("server_logger")


class HttpProcessor(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/api/v1/':

            try:
                # Reading the file
                with open('api/v1/data.json', "r+") as fp:
                    file_to_open = json.load(fp)
                    server_logger.info('Файл "data.json" успешно прочитан')
                    fp.truncate(0)
                    server_logger.info(
                        'Файл "data.json" очищен от предыдущих записей')

                self.send_response(200)
                self.send_header("Content-type", "application/json")

            except:
                file_to_open = "Make a new request and refresh the pages"
                self.send_response(404)
                server_logger.warning("Файл 'data.json' пуст или не найден")

            self.end_headers()
            self.wfile.write(bytes(str(file_to_open), 'utf-8'))

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                b'<a href="http://127.0.0.1:5000/api/v1/">Link to json file</a>')

    def do_POST(self):
        if self.path == '/api/v1/':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode()
            server_logger.info(f"Обработка запроса: {body}")
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
                server_logger.info(
                    f"POST запрос выполнен успешно, результат {pars.json_response}")

            except ValueError:
                self.wfile.write(b"Wrong value")
                server_logger.error(ValueError, exc_info=True)
            except TypeError:
                self.wfile.write(b"Wrong type of data")
                server_logger.error(TypeError, exc_info=True)
            except KeyError:
                self.wfile.write(b"Error key")
                server_logger.error(KeyError, exc_info=True)
            except NameError:
                self.wfile.write(b"Error name of method")
                server_logger.error(NameError, exc_info=True)

        else:
            # content_length = int(self.headers['Content-Length'])
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"Wrong address, correct address http://127.0.0.1:5000/api/v1/")
            server_logger.warning("Выполнен POST запрос на неверный url адрес")


def run(server_class=HTTPServer, handler_class=HttpProcessor):
    """
    Функция run() осуществляет запуск веб-сервера
    """
    try:
        server_address = ('localhost', 5000)
        httpd = server_class(server_address, handler_class)
        server_logger.info(f"Сервер {server_address} запущен успешно")
        httpd.serve_forever()
    except:
        server_logger.warning("Сервер остановлен или произошла ошибка")


if __name__ == "__main__":
    run()
