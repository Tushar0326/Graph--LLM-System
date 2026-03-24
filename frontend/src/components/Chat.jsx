import { useState } from "react";

function Chat() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);

  const sendQuery = async () => {
    const res = await fetch("http://localhost:8000/query/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    setResponse(data);
  };

  return (
    <div>
      <input
        placeholder="Ask something..."
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={sendQuery}>Ask</button>

      <pre>{JSON.stringify(response, null, 2)}</pre>
    </div>
  );
}

export default Chat;