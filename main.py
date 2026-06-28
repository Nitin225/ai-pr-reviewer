from fastapi import FastAPI
from github_client import get_pr_diff, post_comment
from ai_reviewer import review_code

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI PR Reviewer is running"}

@app.post("/webhook")
async def webhook(payload: dict):
    action = payload.get("action")
    
    if action == "opened":
        pr_number = payload["pull_request"]["number"]
        repo_name = payload["repository"]["full_name"]
        print(f"New PR #{pr_number} opened in {repo_name}")
        
        diff = get_pr_diff(repo_name, pr_number)
        review = review_code(diff)
        post_comment(repo_name, pr_number, review)
        
        return {"message": "PR received and commented"}
    
    return {"message": "ignored"}

