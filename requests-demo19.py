import requests
from request.auth import HTTPBasicAuth

req = requests.get('http://localhost:',auth=HTTPBasicAuth('username','password'))
print(req.status_code)