import { Container, Form,InputContainer,Header, Page,Select, SelectEstado} from "./styles";
import { Label } from "../../components/Label";
import { Input } from "../../components/Input";
import { Button } from "../../components/Button";
import { useState, useEffect } from "react";
import { api } from "../../services/api"; 
import { FiFile } from 'react-icons/fi';

export function CreateProperty(){


  //estados para armazenar os dados do form
  const [idCondomio,setIDCondominio] = useState(0)
  const [tipo, setTipoImovel] = useState(" ")
  const [usa_preco, setPreco] = useState(0)
  const [area, setArea] = useState(0)
  const [estado, setStatus] = useState("")
  const [recebe_quartos, setQuarto] = useState(0)
  const [recebe_banheiros, setBanheiro] = useState(0)
  
  
  function handleSignUp(){
    //verifica se todos os dados forma inseridos
    if (!idCondomio || !tipo || !usa_preco || !area || !estado || !recebe_quartos || !recebe_banheiros ){

      return (alert("Preencha todos os campos"))
    }

    //converte dados que vieram em instring para number
    const id_condominio = Number(idCondomio)
    const preco = Number(usa_preco)
    const area_total = Number(area)
    const num_quartos = Number(recebe_quartos)
    const num_banheiros = Number(recebe_banheiros)
 
    //envia os dados para a base de dados
    api.post("/imovel/cadastrar", { tipo, preco, area_total,num_quartos, num_banheiros, id_condominio, status: estado })
    .then(() => {
      alert("Imóvel cadastrado")
    }).catch(error => {
      if (error.response){
        alert(error.response.data.message)
      }else{
        alert("Não foi possível cadastrar")
      }
    })
  }

  const [condominium, setCondominium] = useState([]);
   // Efeito para buscar a lista de condomínios assim que o componente é montado
  useEffect(() => {
    async function fetchProperties() {
      try {
        //busca os dados de condominios cadastrados
        const response = await api.get("/condominio/listar");
        setCondominium(response.data.condominios);
      } catch (error) {
        if (error){
          alert(error.response.data.message)
        }
        console.error("Erro ao buscar imóveis:", error);
      }
    }
  
    fetchProperties(); 
  }, []); //executa sempe que o componentee é renderizado
  console.log(idCondomio)
  return(
    <Container>

      <Page>

        <Header>
          <h1>Cadastro de Imóvel</h1>
          <p>Preencha o formulário abaixo para cadastrar um novo imóvel</p>
        </Header>

        <Form>
          
          <legend>Informações Gerais</legend>

          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={""}>Condomínio</Label>

            
              <Select key = {condominium.id} id="estadoCivil" name="estadoCivil" onChange = {e => setIDCondominio(e.target.value)}>
                {condominium.map((condominium) => (
                  <option Value = {condominium.id}>
                    {condominium.nome}
                  </option>
                ))} 
                </Select>
            
              </div>
            <div >
              <Label htlmFor={"tipo_imovel"}>Tipo do Imóvel</Label>
                <Select onChange = {e => setTipoImovel(e.target.value)}>
                  <option value="Sobrado">Sobrado</option>
                  <option value="Apartamento">Apartamento</option>
                  <option value="Bangalô">Bangalô</option>
                  <option value="Apartamento">Apartamento</option>
                  <option value="Casa Geminada">Casa Geminada</option>

                </Select>
            </div>
          </InputContainer>
          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"preco"}>Preço</Label>
              <Input 
                width={"30rem"}
                placeholder = "R$"
                type = "number"
                id = "preco"
                onChange = {e => setPreco(e.target.value)}
              />
            </div>
            <div >
              <Label htlmFor={"area"}>Área</Label>
                <Input 
                  placeholder="M²"
                  width={"30rem"}
                  type = "number"
                  onChange = {e => setArea(e.target.value)}
                  />
            </div>
          </InputContainer>

          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"quartos"}>Número de Quartos</Label>
              <Input 
                width={"30rem"}
                placeholder = "Nº Quartos"
                type = "number"
                id = "quartos"
                onChange = {e => setQuarto(e.target.value)}
              />
            </div>
            <div >
              <Label htlmFor={"banheiros"}>Número de Banheiros</Label>
                <Input 
                  width={"30rem"}
                  placeholder = "Nº Banheiros"
                  type = "number"
                  onChange = {e => setBanheiro(e.target.value)}
                  />
            </div>
          </InputContainer>
          <div>
          <Label htlmFor={"status"}>Estado do Imóvel</Label>
            <SelectEstado id="estadoCivil" name="estadoCivil" onChange = {e => setStatus(e.target.value)}>
            <option value="Novo">Novo</option>
            <option value="Necessita de reparos">Necessita de reparos</option>
            <option value="Restaurado">Restaurado</option>
          </SelectEstado>
          </div>
          <InputContainer>
            <div className= "chooseFiles">
              <Label htlmFor={"images"}>Imagens</Label>
              <Input 
                width={"62.2rem"}
                type="file"
                multiple
                icon={FiFile}
              />
            </div>
          </InputContainer>

          <Button title={"Cadastrar"} onClick = {handleSignUp}/>

        </Form>

      </Page>
 
    </Container>
  )
}
