import Graph from "./components/Graph";
import Chat from "./components/Chat";

function App() {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
  
  {/* Graph */}
  <div style={{ width: "50%", background: "#0f172a" }}>
    <Graph />
  </div>

  {/* Chat */}
  <div style={{ width: "50%", padding: "20px", background: "#f9fafb" }}>
    <Chat />
  </div>
    </div>
  );
}

export default App;