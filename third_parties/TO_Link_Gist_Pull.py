import requests
import json

def scrape_TO_linkedin_gist(gist_json: str):
    
    gist_response = requests.get(gist_json)
    data = gist_response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data
    

print(scrape_TO_linkedin_gist('https://gist.githubusercontent.com/TJO1225/d7799663f922a813f79ee7293a04c491/raw/c448337d354d469a4f13810d07ebc6a8d1802a69/TO_Link.json'))