import { RiShutDownLine } from "react-icons/ri";
import { Container, Logout } from "./styles";
import { useAuth } from "../../hook/auth";
import { Link } from "react-router-dom";


// * Este componente representa o cabeçalho da aplicação. 
//  * Ele contém links de navegação e um botão de logout.
export function Header () {
  const {signOut} = useAuth() // Usa o hook de autenticação para obter a função de logout

  return (
    <Container>
        <h2>G4</h2>

        <nav>
          <ul>
            <li> <a href="#">Imóveis</a></li>
            <li>
             <a href="#">Área do Cliente</a>

             <ul className="DropDown">
              <li><a href="#">Compras</a></li>
              <li>
                <Link to="/perfil">
                  Meus Dados
                </Link>
              </li>
             </ul>
            </li>
          </ul>
        </nav>
    

      <Logout onClick={signOut}>
        <RiShutDownLine/>
       
      </Logout>

    </Container>
  )
}
