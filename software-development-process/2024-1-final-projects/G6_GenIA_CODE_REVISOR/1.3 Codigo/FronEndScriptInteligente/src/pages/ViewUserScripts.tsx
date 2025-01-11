import React, { useState } from "react";
import { getAnalysis } from "../services/userService";
import { Analysis } from "../services/userService";
import "../styles/form.css";

const ViewAnalysis: React.FC = () => {
  const [scriptId, setScriptId] = useState("");
  const [analysis, setAnalysis] = useState<Analysis[]>([]);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const token = localStorage.getItem("token");
    if (!token) {
      setErrorMessage("Usuário não autenticado");
      return;
    }

    try {
      const analysisData = await getAnalysis(token, parseInt(scriptId));
      setAnalysis(analysisData);
      setErrorMessage("");
      setSuccessMessage("Análise recuperada com sucesso!");
    } catch (error) {
      setErrorMessage("Erro ao recuperar análise. Tente novamente.");
      setSuccessMessage("");
    }
  };

  return (
    <div className="form-container">
      <h2>Visualizar Análise de Scripts</h2>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label htmlFor="scriptId">ID do Script:</label>
        <input
          type="text"
          id="scriptId"
          value={scriptId}
          onChange={(e) => setScriptId(e.target.value)}
          required
        />
        <button type="submit">Visualizar Análise</button>
      </form>
      {analysis.length > 0 && (
        <div className="analysis-results">
          <h3>Resultados da Análise</h3>
          <ul>
            {analysis.map((result, index) => (
              <li key={index}>{result.result}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ViewAnalysis;
