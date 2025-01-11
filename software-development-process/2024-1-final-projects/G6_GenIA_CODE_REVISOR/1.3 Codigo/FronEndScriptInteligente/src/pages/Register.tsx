import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createUser } from "../services/userService";
import "../styles/form.css";

interface RegisterProps {
  onRegister: (userType: string) => void;
}

const Register: React.FC<RegisterProps> = ({ onRegister }) => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [userType, setUserType] = useState("");
  const [protocol, setProtocol] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const navigate = useNavigate();

  const validatePassword = (password: string) => {
    const lengthCheck = password.length >= 8 && password.length <= 40;
    // const numberCheck = /\d.*\d/.test(password);
    // const specialCharCheck = /[!@#$%^&*(),.?":{}|<>]/.test(password);
    // const upperCaseCheck = /[A-Z]/.test(password);
    // const lowerCaseCheck = /[a-z]/.test(password);
    return lengthCheck;
    //   numberCheck &&
    //   specialCharCheck &&
    //   upperCaseCheck &&
    //   lowerCaseCheck
  };

  const handleUserTypeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setUserType(e.target.value);
    setProtocol(""); // Limpar o valor do protocolo quando o tipo de usuário mudar
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(userType); // Adicione esta linha para verificar o valor do userType
    if (!validatePassword(password)) {
      setErrorMessage(
        "A senha deve ter entre 8 e 40 caracteres, incluindo pelo menos 2 números, 1 caractere especial, 1 letra maiúscula e 1 letra minúscula."
      );
      setSuccessMessage("");
      return;
    }

    if (!userType) {
      setErrorMessage("Por favor, selecione um tipo de usuário.");
      setSuccessMessage("");
      return;
    }

    if (
      (userType === "admin" && protocol !== "admin123") ||
      (userType === "employee" && protocol !== "employee123")
    ) {
      setErrorMessage("Protocolo inválido.");
      setSuccessMessage("");
      return;
    }

    try {
      await createUser({
        username: name,
        password,
        role: userType.toUpperCase(),
      });
      setErrorMessage("");
      setSuccessMessage("Registro realizado com sucesso!");
      onRegister(userType);
      if (userType === "user") {
        navigate("/user-home");
      } else if (userType === "employee") {
        navigate("/employee-dashboard");
      } else if (userType === "admin") {
        navigate("/admin-dashboard");
      }
    } catch (error) {
      setErrorMessage("Erro ao registrar usuário. Tente novamente.");
      setSuccessMessage("");
    }
  };

  return (
    <div className="form-container">
      <h2>Registro</h2>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Nome de Usuário:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
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
        <label htmlFor="userType">Tipo de Usuário:</label>
        <select
          id="userType"
          value={userType}
          onChange={handleUserTypeChange}
          required
        >
          <option value="">Selecione</option>
          <option value="user">Usuário</option>
          <option value="admin">Administrador</option>
          <option value="employee">Funcionário</option>
        </select>
        {userType === "admin" && (
          <>
            <label htmlFor="protocol">Protocolo de Administrador:</label>
            <input
              type="text"
              id="protocol"
              value={protocol}
              onChange={(e) => setProtocol(e.target.value)}
              required
            />
          </>
        )}
        {userType === "employee" && (
          <>
            <label htmlFor="protocol">Protocolo de Funcionário:</label>
            <input
              type="text"
              id="protocol"
              value={protocol}
              onChange={(e) => setProtocol(e.target.value)}
              required
            />
          </>
        )}
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
};

export default Register;
