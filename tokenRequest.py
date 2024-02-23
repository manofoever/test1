import requests

class tokenRequest:
    def __init__(self,url):
        self.url = url

    def request_token(self):
        payload = {}
        headers = {}

        response = requests.request("POST",self.url, headers=headers, data=payload, verify=False)

        return response.text