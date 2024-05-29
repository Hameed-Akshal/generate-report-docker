import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    params = {
        "sort": "downloads",
        "direction": -1,  
        "limit": 10       
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        models = response.json()
        
        report = []
        for model in models:
            report.append({
                'modelId': model.get('modelId'),
                'downloads': model.get('downloads', 0)
            })
        
        with open('top_models_report.json', 'w') as f:
            json.dump(report, f, indent=4)
    else:
        print(f"Failed to fetch models: {response.status_code}")

if __name__ == "__main__":
    fetch_top_models()
