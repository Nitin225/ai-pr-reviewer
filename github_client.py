import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization" : f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_pr_diff(repo_name, pr_number):
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}"
    
    diff_headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=diff_headers)
    return response.text

def post_comment(repo_name, pr_number, comment):
    url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"
    
    data = {"body": comment}
    
    response = requests.post(url, headers=headers, json=data)
    return response.status_code