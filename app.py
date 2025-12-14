from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response
from database import save_chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json["message"]
    bot_msg = chatbot_response(user_msg)
    save_chat(user_msg, bot_msg)
    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
