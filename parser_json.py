import json
import logging
from maths import Maths

parser_logger = logging.getLogger("parser_logger")


class ParsJson:
    def __init__(self, body):
        """Метод инициализирует конструктор класса ParsJson"""
        self._body = body

    @property
    def json(self):
        """ Метод проверяет наличие полей в json, который был передан в request."""

        keys = ["id", "jsonrpc", "method", "params"]
        for i in keys:
            if len(self._body) != len(keys) or i not in self._body:
                parser_logger.error(KeyError(f"Неправильный ключ {i}"))
                raise KeyError(f"Неправильный ключ {i}")

        return self._body

    @property
    def id(self):
        if not isinstance(self.json['id'], int):
            parser_logger.error(TypeError("id должно быть целым числом"))
            raise TypeError("id должно быть целым числом")

        if self.json['id'] <= 0:
            parser_logger.error(ValueError(
                "id не должен быть меньше или равен нулю"))
            raise ValueError("id не должен быть меньше или равен нулю")

        return self.json['id']

    @property
    def jsonrpc(self):
        if type(self.json['jsonrpc']) != str:
            parser_logger.error(TypeError("Неправильный тип данных в jsonrpc"))
            raise TypeError("Неправильный тип данных в jsonrpc")

        if self.json['jsonrpc'] != "2.0":
            parser_logger.error(ValueError("Неправильная версия jsonrpc"))
            raise ValueError("Неправильная версия jsonrpc")

        return self.json['jsonrpc']

    @property
    def method(self):
        result = Maths(self.a, self.b)
        name_func = {"divide": result.divide,
                     "add": result.add,
                     "mull": result.mull,
                     "sub": result.sub,
                     }
        for i in name_func:

            if self.json['method'] == i:
                return name_func[i]
        parser_logger.error(NameError("Имя метода введено неправильно!"))
        raise NameError("Имя метода введено неправильно!")

    @property
    def params(self):
        if not isinstance(self.json['params'], list):
            raise TypeError("Неверный тип данных")

        elif len(self.json['params']) != 2:
            parser_logger.error(ValueError(
                "Неверно задано значение поля params"))
            raise ValueError("Неверно задано значение поля params")

        else:
            return self.json['params']

    @property
    def a(self):
        return self.__valid_data(self.params[0])

    @property
    def b(self):
        return self.__valid_data(self.params[1])

    def __valid_data(self, value):
        """Метод проверяет, чтобы переданные значения были либо int, либо float """
        if isinstance(value, (int, float)):
            return value
        else:
            parser_logger.error(TypeError("Неверный тип данных"))
            raise TypeError("Неверный тип данных")

    @property
    def json_data(self):
        """Метод возвращает json ответ в виде строки """
        data = {
            "jsonrpc": self.jsonrpc,
            "result": self.method,
            "id": self.id
        }
        return data

    @property
    def json_response(self):
        return json.dumps(self.json_data)

    def generate_link(self):
        try:
            with open('api/v1/data.json', 'w') as fp:
                json.dump(self.json_data, fp)

        except (FileNotFoundError):
            parser_logger.error(FileNotFoundError("Файл не найден"))
            raise FileNotFoundError("Файл не найден")

        except (FileExistsError):
            parser_logger.error(FileExistsError("Ошибка записи файла"))
            raise FileExistsError("Ошибка записи файла")
