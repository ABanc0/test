import requests
import ssl
import datetime
import socket

check_ssl = [
    'www.eauditor.eu'
]

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'
    context=ssl.create_default_context()
    context.check_hostname = False
    con=context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )

    con.settimeout(10)
    con.connect((hostname, 443))
    ssl_info = con.getpeercert()
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

if __name__ == "__main__":
    for nazwa in check_ssl:
        dzisiejsza_data = datetime.datetime.now()
        try:
            data_wygasniecia = ssl_expiry_datetime(nazwa)
            roznica = data_wygasniecia - dzisiejsza_data
            print ("Nazwa domeny: {} Data wygasniecia: {} Dni do wygasniecia: {}".format(nazwa, data_wygasniecia.strftime("%Y-%m-%d") ,roznica.days))
        except Exception as e:
            print (e)


