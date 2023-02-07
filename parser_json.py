from maths import Maths
import json


class ParsJson:
    def __init__(self, body):
        """Метод разбирает, присланный json запрос,
         и инициализирует конструктор класса ParsJson"""
        self.id = body['id']
        self.jsonrpc = body["jsonrpc"]
        self.method = body["method"]
        self.a = self.__valid_data(body["params"][0])
        self.b = self.__valid_data(body["params"][1])
    
    def __valid_data(self, value):
        if isinstance(value, (int, float)):
            return value
        raise ValueError("Неверный тип данных")
    
    def __check_method(self) -> int:
        """ Функция проверяет, какой метод нужно вызвать из класса Maths """
        result = Maths(self.a, self.b)
        name_func = {"divide": result.divide,
                     "add": result.add,
                     "mull": result.mull,
                     "sub": result.sub,
                     }
        for i in name_func:
            if self.method == i:
                return name_func[i]
    
    @property
    def pars_request(self):
        """Метод возвращает json ответ в виде строки """
        data = {
            "jsonrpc": self.jsonrpc,
            "result": self.__check_method(),
            "id": self.id
        }
        
        return json.dumps(data)
