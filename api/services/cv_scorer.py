from openai import OpenAI
import os

class CVScorer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def score(self, cv_text: str, jd_text: str) -> float:
        prompt = f"""
You are a CV screening assistant. Given this CV:
{cv_text}

And this Job Description:
{jd_text}

Give a matching score between 0 to 100 with 1 decimal point.
Only return the score.
"""
        res = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        score = res.choices[0].message.content.strip()
        return float(score)


