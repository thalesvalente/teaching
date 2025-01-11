import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/employeeDashboard.css';
import visualizarScriptIcon from "./images/visualizar_script.ico";
import scriptIcon from "./images/script.ico";
import dadosPerfilIcon from "./images/dados_perfil.ico";

const EmployeeDashboard: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="dashboard-container">
      <h1>Bem-vindo ao Painel do Funcionário</h1>
      <div className="button-grid">
        <button onClick={() => navigate('/edit-profile')}>
          <img src={dadosPerfilIcon} alt="Alterar Dados do Perfil" className="icon" />
          Alterar Dados do Perfil
        </button>
        <button onClick={() => navigate('/user-dashboard')}>
          <img src={scriptIcon} alt="Submissão de Script" className="icon" />
          Corrigir Script
        </button>
        <button onClick={() => navigate('/view-user-scripts')}>
          <img src={visualizarScriptIcon} alt="Visualizar Script do Usuário" className="icon" />
          Visualizar Script do Usuário
        </button>
      </div>
    </div>
  );
};

export default EmployeeDashboard;
