import datetime
import requests
import jwt

class RoutesClient:
    def __init__(self, base_url, key_path, client_id):
        self.base_url = base_url
        self.key_path = key_path
        self.client_id = client_id
        self.token = self.get_token()

    def get_routes(self):
        headers = {'Authorization': 'Bearer ' + self.token.decode('utf-8')}
        params = {'client_id': self.client_id}
        response = requests.get(self.base_url + '/routes', headers=headers, params=params)
        return response.json()

    def get_token(self):
        key = self.get_key()
        expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)
        body = {'exp': expiration}
        return jwt.encode(body, key, algorithm='RS256')

    def get_key(self):
        key_file = open(self.key_path, 'r')
        return key_file.read()
