import requests


class RequestClient:
    
    def __init__(self, base_url: str, **params) -> None:
        self.base_url = base_url
        self.params = params
    
    def generate_url(self) -> str:
        url = "{}?".format(self.base_url)
        for key in self.params:
            url += "{}={}".format(key, self.params[key])
            url += "&"
        return url[:-1]

    def get_result(self):
        req = requests.get(self.generate_url())
        try:
            data = req.json()
        except:
            data = {
                "message": "Error",
            }
        return data