from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

# Simple rule-based chatbot knowledge base
knowledge_base = {
    "hi": "Hi there! I am your College ChatBot.",
    "hello": "Hey! I am your college chatbot, I can help you with the queries.",
    "hey": "Hi, how can I help you with 😊",
    "courses": "Bapatla Engineering College offers several courses - CSE, IT, ECE, EEE, CIVIL, MECH and Specialization Courses like Data Science (DS), Artificial Intelligence & Machine Learning (AIML), CyberSecurity (CS).",
    "timings": "Hmm, College starts at 7:30 AM and ends at 1:00 PM.",
    "placements": "Many students over the branches have been placed through On-Campus drives at well-known organizations over the past years.",
    "work":"I work on the 'rule-based' principle.",
    "code":"The EAPCET or EAMCET Code for Bapatla Engineering College is 'BECB'.",
    "girls":"Yes😁, The Girls at BEC are Beautiful.",
    "bec":"Haa, BEC stands for Bapatla Engineering College."
}

@app.route("/")
def home():
    return render_template("index.html")  # serve frontend through Flask

@app.route("/chat", methods=["POST"])
def chat():
    response = "Sorry! I don't have information on this 😓."
    data = request.get_json()
    user_input = data.get("message", "").lower()
    if user_input.startswith("you:"):
        user_input = user_input[4:].strip()
    
    # Check keywords in user input
    for keyword in knowledge_base:
        if keyword in user_input:
            response = knowledge_base[keyword]
            break
    return jsonify({"reply": response})
    

if __name__ == "__main__":
    app.run(debug=True)

