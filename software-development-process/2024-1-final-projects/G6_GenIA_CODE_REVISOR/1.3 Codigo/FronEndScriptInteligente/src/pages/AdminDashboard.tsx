import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/adminDashboard.css";
import gerenciarUsuariosIcon from "./images/gerenciar_usuarios.ico";
import visualizarLogsIcon from "./images/visualizar_logs.ico";
import supervisionarSubmissoesIcon from "./images/supervisionar_submissoes.ico";
import settingsIcon from "./images/settings.ico";
import visualizarScriptIcon from "./images/visualizar_script.ico";
import scriptIcon from "./images/script.ico";
import dadosPerfilIcon from "./images/dados_perfil.ico";

const AdminDashboard: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="dashboard-container">
      <h1>Bem-vindo ao Painel do Administrador</h1>
      <div className="button-grid">
        <button onClick={() => navigate("/edit-profile")}>
          <img src={dadosPerfilIcon} alt="Alterar Dados do Perfil" className="icon" />
          Alterar Dados do Perfil
        </button>
        <button onClick={() => navigate("/user-dashboard")}>
          <img src={scriptIcon} alt="Submissão de Script" className="icon" />
          Submissão de Script
        </button>
        <button onClick={() => navigate("/view-user-scripts")}>
          <img src={visualizarScriptIcon} alt="Visualizar Script do Usuário" className="icon" />
          Visualizar Script do Usuário
        </button>
        <button onClick={() => navigate("/configure-integrations")}>
          <img src={settingsIcon} alt="Configurar Integrações" className="icon" />
          Configurar Integrações do Sistema
        </button>
        <button onClick={() => navigate("/manage-users")}>
          <img src={gerenciarUsuariosIcon} alt="Gerenciar Usuários" className="icon" />
          Gerenciar todos os perfis
        </button>
        <button onClick={() => navigate("/manage-scripts")}>
          <img src={supervisionarSubmissoesIcon} alt="Supervisionar Submissões" className="icon" />
          Supervisionar todas as submissões
        </button>
        <button onClick={() => navigate("/audit-activities")}>
          <img src={visualizarLogsIcon} alt="Auditar Atividades" className="icon" />
          Auditar Atividades do Sistema
        </button>
        <button onClick={() => navigate("/system-maintenance")}>
          Backup e Manutenção do Sistema
        </button>
      </div>
    </div>
  );
};

export default AdminDashboard;
