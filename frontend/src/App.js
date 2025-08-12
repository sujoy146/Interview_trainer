import React, { useState } from "react";
import "./App.css";

// Get the backend URL from the environment variable
const BACKEND_URL = process.env.REACT_APP_API_URL;

function App() {
  const [step, setStep] = useState(1);
  const [inputText, setInputText] = useState("");
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState("");
  const [results, setResults] = useState([]);

  const handleStart = async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/api/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: inputText }),
      });
      if (!response.ok) throw new Error(`Server error: ${response.status}`);
      const data = await response.json();
      if (Array.isArray(data.questions)) {
        setQuestions(data.questions);
        setStep(2);
      } else {
        alert("⚠️ Backend returned no questions.");
      }
    } catch (err) {
      console.error("❌ Error generating questions:", err);
      alert("Failed to connect to backend. Is Flask running on port 8080?");
    }
  };

  const handleSubmitAnswer = async () => {
    const question = questions[currentQuestionIndex];
    try {
      const response = await fetch(`${BACKEND_URL}/api/evaluate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, answer }),
      });
      if (!response.ok) throw new Error(`Server error: ${response.status}`);
      const data = await response.json();
      const newResults = [
        ...results,
        {
          question,
          answer,
          feedback: data.feedback || "No feedback provided",
        },
      ];
      setResults(newResults);
      setAnswer("");
      setFeedback("");
      if (currentQuestionIndex + 1 < questions.length) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
      } else {
        setStep(3);
      }
    } catch (err) {
      console.error("❌ Error evaluating answer:", err);
      alert("Evaluation failed. Try again later.");
    }
  };

  // Step 1: Input resume or job description
  if (step === 1) {
    return (
      <div className="App">
        <h2>Interview Trainer Agent</h2>
        <p>
          Enter your resume (or job description / title). The system will generate personalized interview questions.
        </p>
        <textarea
          rows={8}
          placeholder="Paste your resume, experience, or job role here..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <br />
        <button onClick={handleStart} disabled={!inputText.trim()}>
          Generate Questions
        </button>
      </div>
    );
  }

  // Step 2: Question answering
  if (step === 2 && questions.length > 0) {
    const question = questions[currentQuestionIndex];
    return (
      <div className="App">
        <h2>Interview Trainer Agent</h2>
        <div>
          <strong>
            Question {currentQuestionIndex + 1} of {questions.length}:
          </strong>
          <div style={{ margin: "1rem 0" }}>{question}</div>
          <textarea
            rows={4}
            placeholder="Type your answer here..."
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />
          <br />
          <button onClick={handleSubmitAnswer} disabled={!answer.trim()}>
            Submit Answer
          </button>
        </div>
      </div>
    );
  }

  // Step 3: Show feedback/results
  if (step === 3) {
    return (
      <div className="App">
        <h2>Results & Feedback</h2>
        {results.map((r, i) => (
          <div key={i} style={{ marginBottom: "1.5rem", borderBottom: "1px solid #eee", paddingBottom: "1rem" }}>
            <div>
              <strong>Q{i + 1}:</strong> {r.question}
            </div>
            <div>
              <strong>Your Answer:</strong> {r.answer}
            </div>
            <div>
              <strong>Feedback:</strong> {r.feedback}
            </div>
          </div>
        ))}
        <button onClick={() => window.location.reload()}>Start Over</button>
      </div>
    );
  }

  return null; // should never reach here
}

export default App;
