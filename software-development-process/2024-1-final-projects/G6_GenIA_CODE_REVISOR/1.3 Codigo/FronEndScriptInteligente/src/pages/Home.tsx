import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/home.css';
import logo from './images/logo.png';

const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <img src={logo} alt="Company Logo" className="logo" />
      <h1>Bem-vindo ao Script Inteligente</h1>
      <div className="home-options">
        <button onClick={() => navigate('/login')}>Login</button>
        <button onClick={() => navigate('/register')}>Register</button>
      </div>
    </div>
  );
};

export default Home;
