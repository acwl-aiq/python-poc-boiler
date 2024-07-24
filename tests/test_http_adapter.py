import pytest
from boilerplate.http.http_adapter import HttpAdapter

@pytest.mark.functional
def test_http_get():
    adapter = HttpAdapter()
    resp = adapter.http_get("https://httpbin.org/get", {"test_get_param_1": 1, "test_get_param_2": 2})
    #print(resp.text)

@pytest.mark.functional
def test_http_post():
    adapter = HttpAdapter()
    resp = adapter.http_post("https://httpbin.org/post", {"test_post_param_1": 1, "test_post_param_2": 2})
    #print(resp.text)
