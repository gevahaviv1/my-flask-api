from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
contents = {"Summarize": "Summarize the following text:",
            "Ask": "Answer this question:",
            "Search": "Perform a web search and return the most relevant results."}
models = {"Summarize": "gpt-4o",
            "Ask": "gpt-4o",
            "Search": "gpt-4o-search-preview"}

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    text = file.read().decode("utf-8")
    ai_response = send_to_ai(text, "Summarize")
    return jsonify({"summary": ai_response}), 200

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]
    ai_response = send_to_ai(user_message, "Ask")
    return jsonify({"response": ai_response}), 200

@app.route("/search", methods=["GET"])
def web_search():
    query = request.args.get("q")
    ai_response = send_to_ai(query, "Search")
    return jsonify({"results": ai_response}), 200

def send_to_ai(text, action):
    response = openai.ChatCompletion.create(model=models[action], messages=[{"role": "system", "content": contents[action]}, {"role": "user", "content": text}], max_tokens=100)
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    app.run(debug=True)
