import { useEffect, useState } from "react";
import { ForceGraph2D } from "react-force-graph";

function Graph() {
  const [data, setData] = useState({ nodes: [], links: [] });

  useEffect(() => {
    fetch("http://localhost:8000/graph/")
      .then((res) => res.json())
      .then((resData) => {
        // convert backend format → graph format
        const nodes = resData.nodes.map(([id, attr]) => ({
          id,
          ...attr,
        }));

        const links = resData.edges.map(([source, target, attr]) => ({
          source,
          target,
          ...attr,
        }));

        setData({ nodes, links });
      });
  }, []);

  return <ForceGraph2D graphData={data} />;
}

export default Graph;