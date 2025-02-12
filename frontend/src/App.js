import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [health, setHealth] = useState(null);

  useEffect(() => {
    // Fetch the backend health endpoint using the environment variable
    fetch(`${process.env.REACT_APP_API_URL}/health/`)
      .then(response => response.json())
      .then(data => setHealth(data))
      .catch(error => console.error('Error fetching health:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to CircuitCart</h1>
        {health ? (
          <p>Backend Health: {health.status}</p>
        ) : (
          <p>Loading backend status...</p>
        )}
      </header>
    </div>
  );
}

export default App;