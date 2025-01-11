import React, { useState, useEffect } from "react";
import { createApi, getAllApis, deleteApi } from "../services/userService";

const ConfigureIntegrations: React.FC = () => {
  const [apis, setApis] = useState([]);
  const [newApi, setNewApi] = useState({ name: "", url: "" });
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  useEffect(() => {
    const fetchApis = async () => {
      const token = localStorage.getItem("token");
      if (token) {
        try {
          const apis = await getAllApis(token);
          setApis(apis);
        } catch (error) {
          setErrorMessage("Erro ao buscar APIs.");
        }
      }
    };
    fetchApis();
  }, []);

  const handleCreateApi = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado.");
      return;
    }

    try {
      await createApi(token, newApi);
      const apis = await getAllApis(token);
      setApis(apis);
      setNewApi({ name: "", url: "" });
      setSuccessMessage("API criada com sucesso!");
    } catch (error) {
      setErrorMessage("Erro ao criar API.");
    }
  };

  const handleDeleteApi = async (id: number) => {
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado.");
      return;
    }

    try {
      await deleteApi(token, id);
      const apis = await getAllApis(token);
      setApis(apis);
      setSuccessMessage("API deletada com sucesso!");
    } catch (error) {
      setErrorMessage("Erro ao deletar API.");
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Painel do Administrador</h1>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}
      <div>
        <h2>APIs de Correção</h2>
        <div className="form-container">
          <input
            type="text"
            placeholder="Nome da API"
            value={newApi.name}
            onChange={(e) => setNewApi({ ...newApi, name: e.target.value })}
          />
          <input
            type="text"
            placeholder="URL da API"
            value={newApi.url}
            onChange={(e) => setNewApi({ ...newApi, url: e.target.value })}
          />
          <button onClick={handleCreateApi}>Cadastrar API</button>
        </div>
        {/* <ul>
          {apis.map((api) => (
            <li key={api.id}>
              {api.name} - {api.url}
              <button onClick={() => handleDeleteApi(api.id)}>Deletar</button>
            </li>
          ))}
        </ul> */}
      </div>
    </div>
  );
};

export default ConfigureIntegrations;
