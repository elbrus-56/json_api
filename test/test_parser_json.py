import json
import sys
import pytest

sys.path.append("/home/ubuntu/PycharmProjects/json-api/")
from parser_json import ParsJson


class TestParsJson:
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": 8},
         {"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": 8}),
        
        ({"method": "divide", "params": [2, 8], "id": 8, "jsonrpc": "2.0"},
         {"method": "divide", "params": [2, 8], "id": 8, "jsonrpc": "2.0"}),
    ])
    def test_json_with_correct_value(self, var, expected):
        c = ParsJson(var)
        assert c.json == expected
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8]},),
        ({"jsonrpc": "2.0", "method": "divide"},),
        ({"jsonrpc": "2.0"},),
        ({}),
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "asasa": 0},)
    ])
    def test_json_with_wrong_field(self, var):
        with pytest.raises(KeyError):
            ParsJson(var).json
    
    def test_id_with_correct_value(self):
        json_request = {"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": 8}
        c = ParsJson(json_request)
        assert c.id == 8
    
    def test_id_type_value(self):
        json_request = {"jsonrpc": "2.0",
                        "method": "divide", "params": [2, 8], "id": 8}
        c = ParsJson(json_request)
        assert type(c.id) == int
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": "8"}),
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": [9]}),
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": {"k"}}),
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": None}),
    
    ])
    def test_id_with_wrong_type_data(self, var):
        with pytest.raises(TypeError):
            ParsJson(var).id
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": -5}),
    ])
    def test_id_with_negative_number(self, var):
        with pytest.raises(ValueError):
            ParsJson(var).id
    
    def test_jsonrpc_with_correct_data(self):
        json_request = {"jsonrpc": "2.0",
                        "method": "divide", "params": [2, 8], "id": 8}
        c = ParsJson(json_request)
        assert c.jsonrpc == "2.0"
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2,0", "method": "add", "params": [2, 2], "id": 2}),
        ({"jsonrpc": "qwsqwqwqws", "method": "divide", "params": [2, 8], "id": 15}),
        ({"jsonrpc": "", "method": "divide", "params": [2, 8], "id": 5}),
    ])
    def test_jsonrpc_with_wrong_value(self, var):
        with pytest.raises(ValueError):
            ParsJson(var).jsonrpc
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": 2.0, "method": "mull", "params": [2, 3], "id": 3}),
        ({"jsonrpc": (2.0,), "method": "divide", "params": [4, 8], "id": 4}),
        ({"jsonrpc": 2, "method": "sub", "params": [7, 8], "id": 5}),
    ])
    def test_jsonrpc_with_wrong_type_data(self, var):
        with pytest.raises(TypeError):
            ParsJson(var).jsonrpc
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8}, 2),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2, 8], "id": 9}, 16),
        ({"jsonrpc": "2.0", "method": "sub", "params": [8, 6], "id": 99}, 2),
        ({"jsonrpc": "2.0", "method": "add", "params": [2, 8], "id": 55}, 10),
    
    ])
    def test_method(self, var, expected):
        c = ParsJson(var)
        assert c.method == expected
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divid", "params": [4, 2], "id": 8}, 2),
        ({"jsonrpc": "2.0", "method": "mulls", "params": [2, 8], "id": 9}, 16),
        ({"jsonrpc": "2.0", "method": "eruu", "params": [8, 6], "id": 99}, 2),
        ({"jsonrpc": "2.0", "method": 123, "params": [2, 8], "id": 55}, 10),
    
    ])
    def test_wrong_method(self, var, expected):
        with pytest.raises(NameError):
            ParsJson(var).method
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8}, [4, 2]),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2, 8], "id": 9}, [2, 8]),
        ({"jsonrpc": "2.0", "method": "sub", "params": [8, 6], "id": 99}, [8, 6]),
        ({"jsonrpc": "2.0", "method": "add", "params": [2, 8], "id": 55}, [2, 8]),
    
    ])
    def test_params(self, var, expected):
        c = ParsJson(var)
        assert c.params == expected
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, 2, 3], "id": 8}),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2], "id": 9}),
        ({"jsonrpc": "2.0", "method": "sub", "params": [], "id": 99}),
    
    ])
    def test_params_with_wrong_value(self, var):
        with pytest.raises(ValueError):
            ParsJson(var).params
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": (4, 2), "id": 8}),
        ({"jsonrpc": "2.0", "method": "mull", "params": 2, "id": 9}),
        ({"jsonrpc": "2.0", "method": "sub", "params": {2, 3}, "id": 99}),
        ({"jsonrpc": "2.0", "method": "sub", "params": "2, 3", "id": 99}),
    
    ])
    def test_params_with_wrong_type_data(self, var):
        with pytest.raises(TypeError):
            ParsJson(var).params
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8}, 4),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2, 8], "id": 9}, 2),
        ({"jsonrpc": "2.0", "method": "sub", "params": [0, 6], "id": 99}, 0),
        ({"jsonrpc": "2.0", "method": "add", "params": [-1, 8], "id": 55}, -1),
    
    ])
    def test_var_a(self, var, expected):
        c = ParsJson(var)
        assert c.a == expected
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": ["4", 2], "id": 8}),
        ({"jsonrpc": "2.0", "method": "mull", "params": [[2], 4], "id": 9}),
        ({"jsonrpc": "2.0", "method": "sub", "params": [{2}, 3], "id": 7}),
        ({"jsonrpc": "2.0", "method": "add", "params": [None, 4], "id": 6}),
    
    ])
    def test_var_a_with_wrong_type_data(self, var):
        with pytest.raises(TypeError):
            ParsJson(var).a
    
    @pytest.mark.parametrize("var, expected", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8}, 2),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2, 0], "id": 9}, 0),
        ({"jsonrpc": "2.0", "method": "sub", "params": [0, 6], "id": 99}, 6),
        ({"jsonrpc": "2.0", "method": "add", "params": [-1, -8], "id": 55}, -8),
    
    ])
    def test_var_b(self, var, expected):
        c = ParsJson(var)
        assert c.b == expected
    
    @pytest.mark.parametrize("var", [
        ({"jsonrpc": "2.0", "method": "divide", "params": [4, "2"], "id": 8}),
        ({"jsonrpc": "2.0", "method": "mull", "params": [2, [4]], "id": 9}),
        ({"jsonrpc": "2.0", "method": "sub", "params": [2, {3}], "id": 7}),
        ({"jsonrpc": "2.0", "method": "add", "params": [6, None], "id": 6}),
    
    ])
    def test_var_b_with_wrong_type_data(self, var):
        with pytest.raises(TypeError):
            ParsJson(var).b
    
    @pytest.mark.parametrize("var, expected",
                             [({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8},
                               {"jsonrpc": "2.0", "result": 2.0, "id": 8}),
                              ({"method": "add", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 6, "id": 8}),
                              ({"method": "mull", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 8, "id": 8}),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 2, "id": 8})
                              ])
    def test_json_data(self, var, expected):
        assert ParsJson(var).json_data == expected
    
    @pytest.mark.parametrize("var",
                             [({"method": "divide", "params": [4, 2], "id": 8}),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0", 1: 123},),
                              ({},),
                              ([],),
                              ({"method1": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpcs": "2.0"},),
                              ({"method": "sub", "": [4, 2], "id": 8, "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": (4, 2), "id": 8, "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": ["4", 2], "id": 8, "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": [4, "2"], "id": 8, "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": [4, 2], "id": "8", "jsonrpc": "2.0"},),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": 2.0},),
                              ({"method": ["sub"], "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),
                              ({"method": None, "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),
    
                              ])
    def test_json_with_wrong_data(self, var):
        with pytest.raises(KeyError):
            ParsJson(var).json_data
    
    @pytest.fixture()
    def generate_json_file(self, request):
        return ParsJson(request.param).generate_link()
    
    @pytest.mark.parametrize("generate_json_file, expected",
                             [({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8},
                               {"jsonrpc": "2.0", "result": 2.0, "id": 8}),
                              ({"method": "add", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 6, "id": 8}),
                              ({"method": "mull", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 8, "id": 8}),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               {"jsonrpc": "2.0", "result": 2, "id": 8})
                              ],
                             indirect=['generate_json_file'])
    def test_generate_link(self, generate_json_file, expected):
        generate_json_file
        with open("api/v1/data.json", "r") as fp:
            file = json.load(fp)
        assert file == expected
    
    @pytest.mark.parametrize("generate_json_file",
                             [{"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8}
                              ], indirect=['generate_json_file'])
    def test_generate_link_with_wrong_path(self, generate_json_file):
        generate_json_file
        with pytest.raises(FileNotFoundError):
            with open("1/data.json", "r") as fp:
                json.load(fp)
    
    @pytest.fixture()
    def generate_json_response(self, request):
        return ParsJson(request.param).json_response
    
    @pytest.mark.parametrize("generate_json_response, expected",
                             [({"jsonrpc": "2.0", "method": "divide", "params": [4, 2], "id": 8},
                               '{"jsonrpc": "2.0", "result": 2.0, "id": 8}'),
                              ({"method": "add", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               '{"jsonrpc": "2.0", "result": 6, "id": 8}'),
                              ({"method": "mull", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               '{"jsonrpc": "2.0", "result": 8, "id": 8}'),
                              ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},
                               '{"jsonrpc": "2.0", "result": 2, "id": 8}')
                              ],
                             indirect=['generate_json_response'])
    def test_json_response(self, generate_json_response, expected):
        response = generate_json_response
        assert response == expected
