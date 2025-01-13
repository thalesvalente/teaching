import { Routes, Route} from "react-router-dom";
import { SignIn } from "../pages/SignIn";
import { SignUp } from "../pages/SignUp";

// Define as rotas específicas de autenticação
export function AuthRoutes(){
  return(
     <Routes>
      <Route path="/" element = {<SignIn/>}/>
      <Route path="/cadastrar" element = {<SignUp/>}/>
    </Routes>
  )
}