import requests

r = requests.get('file:///C:/D/Python/Pytest/_3_Testing_API/python_qa_api-master/2_requests_json/index.html', auth=('grant', 'password'))
# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)

print(r.text)

print(r.json())


