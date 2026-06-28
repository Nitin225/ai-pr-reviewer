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
        print(f"Diff fetched: {len(diff)} characters")  # add karo
        
        review = review_code(diff)
        print(f"Review generated: {review[:100]}")  # add karo
        
        result = post_comment(repo_name, pr_number, review)
        print(f"Comment post status: {result}")  # add karo
        
        return {"message": "PR reviewed and commented"}
        
    return {"message": "ignored"}

