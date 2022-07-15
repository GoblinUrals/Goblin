from requests import get
import json

url = 'http://ipinfo.io/json'
response = get(url)
data = json.loads(response.text)

city = data['city']
region = data['region']
country = data['country']
postal = data['postal']
timezone = data['timezone']
ip = data['ip']

print('ip:', ip)
print('city:', city)
print('region:', region)
print('country:', country)
print('postal:', postal)
print('timezone:', timezone)


OUTPUT: ip: 93.171.160.45
        city: Minsk
        region: Minsk City
        country: BY
        postal: 223056
        timezone: Europe/Minsk