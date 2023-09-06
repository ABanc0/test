import requests
import ssl

def check_ssl(URL):

    try:
        response = requests.get(URL)
    except requests.exceptions.RequestException as e:
        if 'CERTIFICATE_VERIFY_FAILED' in str(e):
            print(URL +' nie posiada certyfikatu')
        print(URL, f"Nie mozna polaczyc sie ze strona: {str(e)}")
        print('--------------------------')

        return False

    print(URL + " posiada certyfikat")
    return True

