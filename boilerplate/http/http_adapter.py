import requests
from requests import Response


class HttpAdapter:
    def http_post(self, url: str, payload: dict) -> Response:
        return requests.post(url, json=payload)

    def http_get(self, url: str, payload: dict) -> Response:
        return requests.get(url, params=payload)
