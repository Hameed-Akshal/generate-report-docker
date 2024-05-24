import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json()
        sorted_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)
        top_models = sorted_models[:10]
        
        report = []
        for model in top_models:
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
