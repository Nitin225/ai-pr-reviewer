import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def review_code(diff):
    prompt = f"""You are an expert code reviewer.
Review the following code diff and provide:
1. Bugs or errors found
2. Suggestion for improvement
3. Code quality feedback

Code diff: {diff}

Be concise and helpful. """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content