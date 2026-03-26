import { useState } from "react";

function Chat() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendQuery = async () => {
    if (!query.trim()) return;

    const userMessage = { type: "user", text: query };
    setMessages((prev) => [...prev, userMessage]);
    setQuery("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/query/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();

      const botMessage = {
        type: "bot",
        text: data.answer || JSON.stringify(data),
      };

      setMessages((prev) => [...prev, botMessage]);

    } catch {
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "Error occurred!" },
      ]);
    }

    setLoading(false);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>
      
      {/* Chat messages */}
      <div style={{ flex: 1, overflowY: "auto", marginBottom: "10px" }}>
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              textAlign: msg.type === "user" ? "right" : "left",
              margin: "10px",
            }}
          >
            <span
              style={{
                display: "inline-block",
                padding: "10px",
                borderRadius: "10px",
                background:
                  msg.type === "user" ? "#2563eb" : "#e5e7eb",
                color: msg.type === "user" ? "white" : "black",
                maxWidth: "70%",
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}

        {loading && <p>⏳ Thinking...</p>}
      </div>

      {/* Input */}
      <div style={{ display: "flex" }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something..."
          style={{
            flex: 1,
            padding: "10px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
        />

        <button
          onClick={sendQuery}
          style={{
            marginLeft: "10px",
            padding: "10px 15px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "5px",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;