import React from 'react';
import '../styles/adminDashboard.css';

const SystemMaintenance: React.FC = () => {
  const handleBackup = () => {
    alert('Backup do sistema realizado com sucesso!');
  };

  const handleMaintenance = () => {
    alert('Manutenção do sistema realizada com sucesso!');
  };

  return (
    <div className="dashboard-container">
      <h1>Backup e Manutenção do Sistema</h1>
      <button onClick={handleBackup}>Executar Backup</button>
      <button onClick={handleMaintenance}>Executar Manutenção</button>
    </div>
  );
};

export default SystemMaintenance;
