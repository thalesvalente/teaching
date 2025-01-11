import React, { useState, useEffect } from "react";
import {
  getAllScripts,
  updateScript,
  deleteScript,
} from "../services/userService";

interface Script {
  id: number;
  content: string;
  userId: number;
  username: string; // Presume que a API retorna também o nome do usuário
}

const ManageScripts: React.FC = () => {
  const [scripts, setScripts] = useState<Script[]>([]);
  const [filteredScripts, setFilteredScripts] = useState<Script[]>([]);
  const [editScript, setEditScript] = useState<Script | null>(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [searchUsername, setSearchUsername] = useState("");

  useEffect(() => {
    const fetchScripts = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await getAllScripts(token!);
        setScripts(response);
        setFilteredScripts(response); // Inicialmente, sem filtro
      } catch (error) {
        setErrorMessage("Erro ao buscar scripts.");
      }
    };
    fetchScripts();
  }, []);

  const handleEditScript = (script: Script) => {
    setEditScript(script);
  };

  const handleSaveScript = async () => {
    const token = localStorage.getItem("token");
    if (!token || !editScript) {
      setErrorMessage("Usuário não autenticado ou nenhum script selecionado.");
      return;
    }

    try {
      await updateScript(token, editScript.id.toString(), {
        content: editScript.content,
      });
      setSuccessMessage("Script atualizado com sucesso!");
      setEditScript(null);
      const response = await getAllScripts(token);
      setScripts(response);
      setFilteredScripts(response); // Atualiza a lista filtrada
    } catch (error) {
      setErrorMessage("Erro ao atualizar script.");
    }
  };

  const handleDeleteScript = async (id: number) => {
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado.");
      return;
    }

    try {
      await deleteScript(token, id.toString());
      setSuccessMessage("Script deletado com sucesso!");
      const response = await getAllScripts(token);
      setScripts(response);
      setFilteredScripts(response); // Atualiza a lista filtrada
    } catch (error) {
      setErrorMessage("Erro ao deletar script.");
    }
  };

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setSearchUsername(value);

    if (value === "") {
      setFilteredScripts(scripts); // Mostra todos os scripts se o campo de busca estiver vazio
    } else {
      const filtered = scripts.filter((script) =>
        script.username.toLowerCase().includes(value.toLowerCase())
      );
      setFilteredScripts(filtered);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Gerenciar Scripts</h1>
      {errorMessage && <p>{errorMessage}</p>}
      {successMessage && <p>{successMessage}</p>}
      <input
        type="text"
        placeholder="Buscar por nome de usuário"
        value={searchUsername}
        onChange={handleSearchChange}
      />
      <ul>
        {filteredScripts.map((script) => (
          <li key={script.id}>
            <p>Usuário: {script.username}</p>
            <p>Conteúdo: {script.content}</p>
            <button onClick={() => handleEditScript(script)}>Editar</button>
            <button onClick={() => handleDeleteScript(script.id)}>
              Deletar
            </button>
          </li>
        ))}
      </ul>
      {editScript && (
        <div>
          <h2>Editar Script</h2>
          <label>
            Conteúdo:
            <textarea
              value={editScript.content}
              onChange={(e) =>
                setEditScript({ ...editScript, content: e.target.value })
              }
              rows={10}
              cols={50}
            />
          </label>
          <button onClick={handleSaveScript}>Salvar</button>
          <button onClick={() => setEditScript(null)}>Cancelar</button>
        </div>
      )}
    </div>
  );
};

export default ManageScripts;
