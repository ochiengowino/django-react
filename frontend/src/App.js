// import logo from './logo.svg';
import './App.css';
// import Hello from './components/Hello';
import Message from './components/Message';
import Profile from './components/Profile';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
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
      </header> */}
      {/* <Hello></Hello> */}
      <Message messageCont='This is a message'></Message>
      <Profile fname="Jackson" lname="Kent">
        <h3>This is the profile of Jackson</h3>
      </Profile>
      {/* <Profile fname="Janet" lname="Kylie"></Profile>
      <Profile fname="John" lname="Kash"></Profile> */}
    </div>
  );
}

export default App;
