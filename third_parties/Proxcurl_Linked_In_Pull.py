import requests
import json

api_key = 
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/tom-o-loughlin-036803a/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

# Assuming 'response' is the Response object
data = response.json()

# Write to a JSON file
with open('TO_LinkedIn_data.json', 'w') as f:
    json.dump(data, f)

