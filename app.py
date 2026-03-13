from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/")
def index():
    return render_template("index.html", project_name="NexaChat AI")

# Free models to try in order (fallback chain)
FREE_MODELS = [
    "mistralai/mistral-small-3.1-24b-instruct:free",
    "qwen/qwen3-4b:free",
    "google/gemma-3-4b-it:free",
]

@app.route("/api/ask", methods=["POST"])
def ask():
    user_input = request.json.get("prompt", "")

    for model in FREE_MODELS:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": user_input}]
        }

        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
            result = response.json()

            if "error" in result:
                continue  # Try next model

            reply = result["choices"][0]["message"]["content"]
            return jsonify({"response": reply})
        except Exception:
            continue  # Try next model

    return jsonify({"response": "All AI models are temporarily unavailable. Please try again in a moment."})

if __name__ == "__main__":
    app.run(debug=True)
