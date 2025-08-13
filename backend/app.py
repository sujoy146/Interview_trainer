from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_parser import extract_skills_from_resume
from utils.ibm_granite_api import generate_questions, evaluate_answer

app = Flask(__name__)
CORS(app)

@app.before_request
def log_request():
    print("=" * 40)
    print(f"Request: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")
    try:
        print(f"JSON: {request.get_json(force=False, silent=True)}")
    except Exception as e:
        print(f"Error reading JSON: {e}")
    print("=" * 40)

@app.route("/api/generate", methods=["POST"])
def generate():
    if request.method != "POST":
        return jsonify({"error": "Only POST allowed"}), 405

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    input_text = data.get("input", "")
    if not input_text:
        return jsonify({"error": "Input text is required"}), 400

    try:
        if len(input_text.split()) > 10:
            skills = extract_skills_from_resume(input_text)
            context = ", ".join(skills)
        else:
            context = input_text
        questions = generate_questions(context)
        return jsonify({"questions": questions})
    except Exception as e:
        print(f"generate() error: {e}")
        return jsonify({"error": "Server error generating questions"}), 500

@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"}), 400
    question = data.get("question")
    answer = data.get("answer")
    if not question or not answer:
        return jsonify({"error": "Missing question or answer"}), 400

    try:
        feedback = evaluate_answer(question, answer)
        return jsonify({"feedback": feedback})
    except Exception as e:
        print(f"evaluate() error: {e}")
        return jsonify({"error": "Server error during evaluation"}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
