import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [version, setVersion] = useState('');
  const [author, setAuthor] = useState('');
  const [health, setHealth] = useState('');
  const [index, setIndex] = useState('');

  useEffect(async () => {
    fetch('http://api.sa.homework/version').then((res) => setVersion(res));
    fetch('http://api.sa.homework/author').then((res) => setAuthor(res));
    fetch('http://api.sa.homework/health').then((res) => setHealth(res));
    fetch('http://api.sa.homework/').then((res) => setIndex(res));
  }, [version, author, health, index]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>{index}</p>
        <p>Version: {version}</p>

        <p>Health: {health}</p>

        <p>{author}</p>
      </header>
    </div>
  );
}

export default App;
