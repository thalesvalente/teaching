import { BrowserRouter } from "react-router-dom";
import { ClientRoutes } from "./clients.routes";
import { AuthRoutes } from "./auth.routes";
import {EmployeeRoutes } from "./employee.routes";
import { useAuth } from "../hook/auth";

 
// Define o componente de rotas da aplicação
export function Routes(){
  const {user} = useAuth() // Obtém o usuário autenticado do contexto de autenticação

 
  return(
    <BrowserRouter>
      {user ? <EmployeeRoutes/> : <AuthRoutes/> }
       {/* Renderiza EmployeeRoutes se o usuário estiver autenticado, senão renderiza AuthRoutes */}
    </BrowserRouter>
  )
}
