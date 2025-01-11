import React, { useEffect, useState } from 'react';
import '../styles/adminDashboard.css';

interface ActivityLog {
  timestamp: string;
  action: string;
  user: string;
}

const AuditActivities: React.FC = () => {
  const [logs, setLogs] = useState<ActivityLog[]>([]);

  useEffect(() => {
    // Simulação de busca de logs
    const fetchedLogs = [
      { timestamp: '2023-06-01T12:00:00Z', action: 'Login', user: 'admin' },
      { timestamp: '2023-06-01T12:05:00Z', action: 'Edit Profile', user: 'user1' },
    ];
    setLogs(fetchedLogs);
  }, []);

  return (
    <div className="dashboard-container">
      <h1>Auditar Atividades do Sistema</h1>
      <ul>
        {logs.map((log, index) => (
          <li key={index}>{log.timestamp} - {log.action} - {log.user}</li>
        ))}
      </ul>
    </div>
  );
};

export default AuditActivities;
