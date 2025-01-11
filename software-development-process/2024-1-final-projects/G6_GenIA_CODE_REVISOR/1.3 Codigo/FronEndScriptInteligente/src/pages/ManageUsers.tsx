import React, { useState, useEffect } from "react";
import {
  getAllUsers,
  updateUser,
  updateUserRole,
} from "../services/userService";
import "../styles/adminDashboard.css"; // Certifique-se de que o caminho está correto

interface User {
  id: number;
  username: string;
  role: string;
}

const ManageUsers: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [editUser, setEditUser] = useState<User | null>(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [userId, setUserId] = useState<string>("");

  const fetchUsers = async (token: string) => {
    try {
      const response = await getAllUsers(token);
      setUsers(response);
    } catch (error) {
      setErrorMessage("Erro ao buscar usuários.");
    }
  };

  const fetchUserById = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado.");
      return;
    }

    try {
      const response = await getAllUsers(token);
      const user = response.find((user: User) => user.id.toString() === userId);
      if (user) {
        setUsers([user]);
      } else {
        setErrorMessage("Usuário não encontrado.");
        setUsers([]);
      }
    } catch (error) {
      setErrorMessage("Erro ao buscar usuário.");
    }
  };

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      fetchUsers(token);
    }
  }, []);

  const handleEditUser = (user: User) => {
    setEditUser(user);
  };

  const handleSaveUser = async () => {
    const token = localStorage.getItem("token");
    if (!token || !editUser) {
      setErrorMessage("Usuário não autenticado ou nenhum usuário selecionado.");
      return;
    }

    try {
      await updateUser(token, editUser.id.toString(), editUser);
      setSuccessMessage("Informações do usuário atualizadas com sucesso!");
      setEditUser(null);
      fetchUsers(token);
    } catch (error) {
      setErrorMessage("Erro ao atualizar usuário.");
    }
  };

  const handleRoleChange = async (userId: number, role: string) => {
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado.");
      return;
    }

    try {
      await updateUserRole(token, userId.toString(), role);
      setSuccessMessage("Permissão do usuário atualizada com sucesso!");
      fetchUsers(token);
    } catch (error) {
      setErrorMessage("Erro ao atualizar permissão do usuário.");
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Gerenciar Usuários</h1>
      {errorMessage && <p>{errorMessage}</p>}
      {successMessage && <p>{successMessage}</p>}
      
      <div>
        <input
          type="text"
          placeholder="Buscar por ID do usuário"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        />
        <button onClick={fetchUserById}>Buscar</button>
      </div>

      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <p>Nome: {user.username}</p>
            <p>Role: {user.role}</p>
            <button onClick={() => handleEditUser(user)}>Editar</button>
            <select
              value={user.role}
              onChange={(e) => handleRoleChange(user.id, e.target.value)}
            >
              <option value="USER">Usuário</option>
              <option value="EMPLOYEE">Funcionário</option>
              <option value="ADMIN">Administrador</option>
            </select>
          </li>
        ))}
      </ul>
      {editUser && (
        <div>
          <h2>Editar Usuário</h2>
          <label>
            Nome:
            <input
              type="text"
              value={editUser.username}
              onChange={(e) =>
                setEditUser({ ...editUser, username: e.target.value })
              }
            />
          </label>
          <button onClick={handleSaveUser}>Salvar</button>
          <button onClick={() => setEditUser(null)}>Cancelar</button>
        </div>
      )}
    </div>
  );
};

export default ManageUsers;
