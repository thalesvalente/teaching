import { Routes, Route} from "react-router-dom";
import { BrokerHome } from "../pages/BrokerHome";
import { ManagerHome } from "../pages/ManagerHome";
import { EmployeeHome } from "../pages/EmployeeHome";
import { DetailsProperty } from "../pages/DetailsProperty";
import { Properties } from "../pages/Properties";
import { Employees } from "../pages/Employees";
import { CreateEmployee } from "../pages/CreateEmployee";
import { Sales } from "../pages/Sales";
import { CondominiumRegistration } from "../pages/Condominium_registration";
import { CreateProperty } from "../pages/CreateProperty";

// Define as rotas específicas para funcionários
export function EmployeeRoutes(){
  return(
    <Routes>
      <Route path="/" element = {<EmployeeHome/>}/>
      <Route path="/corretor" element = {<BrokerHome/>}/>
      <Route path="/adm" element= {<ManagerHome/>}/>
      <Route path="/imoveis/detalhes" element= {<DetailsProperty/>}/>
      <Route path="/imoveis/listar" element = {<Properties/>}/>
      <Route path="/vendas" element = {<Sales/>}/>
      <Route path="/funcionario/listar" element = {<Employees/>}/>
      <Route path="/funcionario/cadastrar" element = {<CreateEmployee/>}/>
      <Route path ="/condominio/cadastrar" element = {<CondominiumRegistration/>}/>
      <Route path ="/imoveis/cadastrar" element = { <CreateProperty/> }/>
    </Routes>
  )
}
