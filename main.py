import requests


def authorize(login, password):
    http = requests.Session()
    http.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
        }
    )
    r = http.post(
        'https://www.weblancer.net/account/login/',
        data={'login': login, 'password': password, 'store_login': 1},
        headers={'X-Requested-With': 'XMLHttpRequest'}
    ).json()
    if r['result']:
        return http
    else:
        return False


if __name__ == "__main__":
    import pickle
    import time

    SESSION_FILE = 'session.pickle'

    try:
        with open(SESSION_FILE, 'rb') as f:
            http = pickle.load(f)
    except FileNotFoundError:
        print('Please provide Weblance.net credentials')
        while 1:
            login = input('Login: ')
            password = input('Password: ')
            http = authorize(login, password)
            if http:
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(http, f)
                break
            else:
                print('Error: login or password incorrect')

    while 1:
        http.get('https://www.weblancer.net')
        time.sleep(270)
