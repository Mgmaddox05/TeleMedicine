import React, { useState } from 'react';
import MessageSection from './MessageSection';
import './App.css';

function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  const toggleLogin = () => {
    setShowLogin(!showLogin);
    setShowSignup(false);
  };

  const toggleSignup = () => {
    setShowSignup(!showSignup);
    setShowLogin(false);
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>Welcome to Telehealth Services</h1>
      </header>

      <nav className="navbar">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
        <button className="login-button" onClick={toggleLogin}>Login</button>
        <button className="signup-button" onClick={toggleSignup}>Sign Up</button>
      </nav>

      <section className={`login-container ${showLogin ? 'show' : ''}`}>
        <h2>Login</h2>
        <form id="loginForm" action="/login" method="POST">
          <input type="text" id="username" name="username" placeholder="Username" required /><br />
          <input type="password" id="password" name="password" placeholder="Password" required /><br />
          <input type="submit" value="Login" />
        </form>
      </section>

      <section className={`signup-container ${showSignup ? 'show' : ''}`}>
        <h2>Sign Up</h2>
        <form id="signupForm" action="/signup" method="POST">
          <input type="text" id="fullName" name="fullName" placeholder="Full Name" required /><br />
          <input type="email" id="email" name="email" placeholder="Email" required /><br />
          <input type="password" id="signupPassword" name="signupPassword" placeholder="Password" required /><br />
          <input type="submit" value="Sign Up" />
        </form>
      </section>

      <footer className="footer">
        <p>&copy; 2023 Telehealth Services</p>
      </footer>
      <MessageSection />
    </div>
  );
}

export default App;
