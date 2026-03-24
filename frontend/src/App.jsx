import Graph from "./components/Graph";
import Chat from "./components/Chat";

function App() {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      
      {/* Left side → Graph */}
      <div style={{ flex: 1 }}>
        <Graph />
      </div>

      {/* Right side → Chat */}
      <div style={{ flex: 1, padding: "20px" }}>
        <Chat />
      </div>

    </div>
  );
}

export default App;