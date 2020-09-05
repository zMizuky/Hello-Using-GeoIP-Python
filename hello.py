from ip2geotools.databases.noncommercial import DbIpCity
from requests import get
ip = get('https://api.ipify.org').text
response = DbIpCity.get(ip, api_key='free')
print('''
==========================
|  _    _      _ _       |
| | |  | |    | | |      |
| | |__| | ___| | | ___  |
| |  __  |/ _ \ | |/ _ \ |
| | |  | |  __/ | | (_) ||
| |_|  |_|\___|_|_|\___/ |
|                        |
==========================\n''')
print("Your ip:   ", response.ip_address)
print("Country:   ", response.country)
print("Region:    ", response.region)
print("City:      ", response.city)
print("Latitude: ", response.latitude)
print("Longitude:", response.longitude)
print(f"\nHello in {response.country}: ")

if response.country == "US":
    print("Hello")
elif response.country == "BR":
    print("Olá!")
elif response.country == "JP":
    print("こんにちは")
elif response.country == "PT":
    print("Olá")
elif response.country == "MX":
    print("Hola")
elif response.country == "ES":
    print("Hola")
