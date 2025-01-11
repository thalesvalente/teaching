import React from "react";
import { useNavigate } from "react-router-dom";
import jwt_decode from "jwt-decode";
import "../styles/userHome.css";
import scriptIcon from "./images/script.ico";
import dadosPerfilIcon from "./images/dados_perfil.ico";

interface DecodedToken {
  username: string;
}

const UserHome: React.FC = () => {
  const [username, setUsername] = React.useState("");
  const navigate = useNavigate();

  return (
    <div className="user-home-container">
      <h2>Bem-vindo, {username}</h2>
      <div className="home-options">
        <button onClick={() => navigate("/edit-profile")}>
          <img src={dadosPerfilIcon} alt="Alterar Dados do Perfil" className="icon" />
          Alterar Dados do Perfil
        </button>
        <button onClick={() => navigate("/user-dashboard")}>
          <img src={scriptIcon} alt="Submissão de Script" className="icon" />
          Submissão de Script
        </button>
      </div>
    </div>
  );
};

export default UserHome;
