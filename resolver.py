# pip install requests
import requests

# Unique API key and URL of page you want to scrape 
url = 'https://nowsecure.nl/'
apikey = YOUR_API_KEY
params = {
    'url': url,
    'apikey': apikey,
    'js_render': 'true',
    'antibot': 'true',
    'premium_proxy': 'true',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)

print(response.text)
