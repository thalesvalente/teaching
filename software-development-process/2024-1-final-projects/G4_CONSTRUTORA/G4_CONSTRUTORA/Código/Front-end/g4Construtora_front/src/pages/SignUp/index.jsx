import { Container,Form,InputContainer,Select, Header, Page} from "./styles";
import { Input } from "../../components/Input";
import {FiMail,FiLock} from "react-icons/fi"
import { Button } from "../../components/Button";
import { Label } from "../../components/Label";
import { IoIosArrowDown } from "react-icons/io"
import { useState } from "react";
import { api } from "../../services/api";

// Define o componente de cadastro de usuário
export function SignUp(){
  // Estados para armazenar os valores dos campos de entrada
  const [cpf, setCpf] = useState("")
  const [nome, setNome] = useState("")
  const [numeroDeFilhos, setNumerodeFilhos] = useState(0)
  const [estado_civil, setEstadoCivil] = useState("")
  const [renda2, setRenda] = useState(0)

  // Função para lidar com o cadastro
  function handleSignUp(){
     // Verifica se todos os campos estão preenchidos
    if (!cpf || !nome || !numeroDeFilhos || !estado_civil || !renda2){
      return (alert("Preencha todos os campos"))
    }

    const renda = Number(renda2)
    const numero_de_filhos = Number(numeroDeFilhos)
    console.log(typeof renda )
  // Envia os dados para a API
    api.post("/cliente/cadastrar", {cpf, nome,numero_de_filhos,estado_civil,renda})
    .then((data) => {
      alert("Usuário cadastrado")
      console.log(data)
    }).catch(error => {
      if (error.response){
        alert(error.response.data.message)
      }else{
        alert("Não foi possível cadastrar")
      }
    })
  }

  return(
    <Container>
      <Page>
      <Header>
        <h1>G4 Construtora</h1>
        <p>Construa sua vida com a gente</p>
      </Header>
      
      <Form>
        
        <h2>Crie Sua Conta</h2>

        <InputContainer>
          <div className="wrapper">
          
            <Label htlmFor={"name"}>Nome</Label>
            <Input 
              width={"62.2rem"}
              placeholder = "seu nome completo"
              type = "text"
              id = "name"
              onChange = {e => setNome(e.target.value)}
            />
          </div>
        </InputContainer>

        <InputContainer>

          <div>
            <Label htlmFor={"CPF"}>CPF</Label>
            <Input 
              width={"30rem"}
              placeholder = "000.000.000-00"
              type = "text"
              id = "CPF"
              onChange = {e =>setCpf(e.target.value)}
            />
          </div>

          <div>
            <Label htlmFor={""}>N° de Filhos</Label>
            <Input 
              width={"30rem"}
              placeholder = "Quantos filhos você tem?"
              type = "number"
              onChange = {e => setNumerodeFilhos(e.target.value)}
            />
          </div>
        </InputContainer>

        <InputContainer>
          <div>
            <Label htlmFor={""}>Estado Civil</Label>
            <Select id="estadoCivil" name="estadoCivil" onChange = {e => setEstadoCivil(e.target.value)}>
              <option value="solteiro">Solteiro(a)</option>
              <option value="casado">Casado(a)</option>
              <option value="divorciado">Divorciado(a)</option>
              <option value="viuvo">Viúvo(a)</option>
            
            </Select>
          
          </div>

          <div>
            <Label htlmFor={""}>Renda</Label>
            <Input 
              width={"30rem"}
                placeholder = "1000"
                type = "number"
                onChange = {e => setRenda(e.target.value)}
            />
          </div>
          </InputContainer>
          {/* <div>
            <Label htlmFor={""}>E-mail</Label>

            <Input
            width={"47.8rem"}
              placeholder = "E-mail"
              type = "text"
              icon={FiMail}
            />
          </div> */}
          <div>
            <Label htlmFor={""}>Senha</Label>
              <Input
                width={"62.2rem"}
                placeholder = "Senha forte"
                type = "password"
                icon={FiLock}    
            />

          </div>

            
        <Button title={"Cadastrar"} onClick = {handleSignUp}/>
        
        </Form>
        </Page>
    </Container>
  )

}