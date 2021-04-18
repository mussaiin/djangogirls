import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [version, setVersion] = useState('');
  const [author, setAuthor] = useState('');
  const [health, setHealth] = useState('');
  const [index, setIndex] = useState('');

  useEffect(async () => {
    await fetch('http://api.sa.homework/version')
      .then((response) => response.json())
      .then((data) => setVersion(data));
    await fetch('http://api.sa.homework/author')
      .then((response) => response.json())
      .then((data) => setAuthor(data));
    await fetch('http://api.sa.homework/health')
      .then((response) => response.json())
      .then((data) => setHealth(data));
    await fetch('http://api.sa.homework/')
      .then((response) => response.json())
      .then((data) => setIndex(data));
  });

  console.log(version, author, health, index);

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
        <p>{JSON.stringify(index)}</p>
        <p>Version: {JSON.stringify(version)}</p>

        <p>Health: {JSON.stringify(health)}</p>

        <p>{JSON.stringify(author)}</p>
      </header>
    </div>
  );
}

export default App;
