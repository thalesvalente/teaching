import React, { useState } from "react";
import { updateUserProfile } from "../services/userService";
import "../styles/form.css";

const EditProfile: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [profilePicture, setProfilePicture] = useState<File | null>(null);
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
      await updateUserProfile(token, {
        username,
        password,
        profilePicture: profilePicture ? profilePicture.name : undefined,
      });
      setErrorMessage("");
      setSuccessMessage("Perfil atualizado com sucesso!");
    } catch (error) {
      setErrorMessage("Erro ao atualizar perfil. Tente novamente.");
      setSuccessMessage("");
    }
  };

  const handleProfilePictureChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];
    if (file) {
      setProfilePicture(file);
    }
  };

  return (
    <div className="form-container">
      <h2>Editar Perfil</h2>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}
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
        {/* <label htmlFor="profilePicture">Foto de Perfil:</label>
        <input
          type="file"
          id="profilePicture"
          accept="image/*"
          onChange={handleProfilePictureChange}
        /> */}
        <button type="submit">Atualizar Perfil</button>
      </form>
    </div>
  );
};

export default EditProfile;
