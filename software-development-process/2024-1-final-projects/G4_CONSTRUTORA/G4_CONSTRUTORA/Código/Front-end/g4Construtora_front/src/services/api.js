import axios from "axios";

// Cria uma instância do axios com uma configuração básica
export const api = axios.create({
  baseURL : "http://localhost:8080" // Define a URL base para todas as requisições HTTP
}
)