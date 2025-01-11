import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../services/userService";
import "../styles/form.css";

interface LoginProps {
  onLogin: (userType: string) => void;
}

const Login: React.FC<LoginProps> = ({ onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [loggedInUser, setLoggedInUser] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const { access_token } = await loginUser({ username, password });
      localStorage.setItem("token", access_token);
      const decodedToken: any = JSON.parse(atob(access_token.split(".")[1]));
      setErrorMessage("");
      setLoggedInUser(decodedToken.username);
      onLogin(decodedToken.role.toLowerCase());
      if (decodedToken.role.toLowerCase() === "user") {
        navigate("/user-home");
      } else if (decodedToken.role.toLowerCase() === "employee") {
        navigate("/employee-dashboard");
      } else if (decodedToken.role.toLowerCase() === "admin") {
        navigate("/admin-dashboard");
      }
    } catch (error) {
      setErrorMessage("Usuário ou senha inválidos.");
    }
  };

  const handleRegister = () => {
    navigate("/register");
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      {loggedInUser && <p>Bem-vindo, {loggedInUser}!</p>}
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Nome de Usuário:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <label htmlFor="password">Senha:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
