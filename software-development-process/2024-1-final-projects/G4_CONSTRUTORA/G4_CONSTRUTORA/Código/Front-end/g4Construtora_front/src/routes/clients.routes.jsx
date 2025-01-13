import { Routes, Route} from "react-router-dom";
import { ClientHome } from "../pages/Client-Home";
import { Profile } from "../pages/Profile";
import { PropertyDetails } from "../pages/ProperTyDetails";

// Define as rotas específicas para clientes
export function ClientRoutes(){
  return(
    <Routes>
      <Route path="/" element = {<ClientHome/>}/>
      <Route path="/perfil" element = {<Profile/>}/>
      <Route path="/imovel/:id" element = {<PropertyDetails/>}/>
    </Routes>
  )
}