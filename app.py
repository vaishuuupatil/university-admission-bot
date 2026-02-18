from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Admission Bot Knowledge Base
responses = {
    "hello": "Hello! Welcome to University Admission Bot. How can I help you?",
    "hi": "Hi! Ask me anything about university admissions.",
    "admission": "Admission process usually starts in June and ends in August.",
    "fees": "Average yearly fees is around ₹50,000 depending on the course.",
    "documents": "Required documents are 10th marksheet, 12th marksheet, ID proof, and passport size photo.",
    "courses": "We offer BCA, BBA, BSc IT, Engineering and Management courses.",
    "scholarship": "Scholarships are available based on merit and category.",
    "contact": "You can contact admission office at 9876543210."
}

# Bot Logic
def get_bot_response(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return responses[key]

    return "Sorry, I didn't understand. Please ask about admission, fees, courses, or documents."

# API Route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_reply = get_bot_response(user_message)

    return jsonify({"reply": bot_reply})

# Run Server
if __name__ == "__main__":
    app.run(debug=True)

