from fastapi import FastAPI
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
        return {"message": "PR received"}
    
    return {"message": "ignored"}