import { Container, Form,InputContainer,Header, Page,Select} from "./styles";
import { Label } from "../../components/Label";
import { Input } from "../../components/Input";
import { Button } from "../../components/Button";
import { useState, useEffect} from "react";
import { api } from "../../services/api"; 
import axios from "axios";

export function CondominiumRegistration(){

  //estados para armazenar os dados inseridos no formulário
  const [nome,setNome] = useState("")
  const [quantideImoveis, setQuantidadeImoveis] = useState(0)
  const [amenidades, setAmenidades] = useState("")
  const [usa_taxa, setTaxa] = useState(0)
  const [anoConstrução, setAnoConstrução] = useState(0)
  const [status, setStatus] = useState("")
  const [rua, setRua] = useState("")
  const [recebe_numero, setNumero] = useState(0)
  const [cidade, setCidade] = useState("")
  const [estado, setEstado] = useState("")
  const [cep, setCep] = useState("")
  
  function handleSignUp(){
    //verifica se todos os dados foram inseridos
    if (!quantideImoveis || !nome || !amenidades || !usa_taxa || !anoConstrução || !status || !rua || !recebe_numero || !cidade || !estado || !cep ){
      return (alert("Preencha todos os campos"))
    }
    //conversão de string pra number
    const quantidade_imoveis = Number(quantideImoveis)
    const taxa = Number(usa_taxa)
    const ano_construcao = Number(anoConstrução)
    const numero = Number(recebe_numero)


    //faz a requisição para a api, enviando os dados para a base de dados
    api.post("/condominio/cadastrar", {quantidade_imoveis, taxa,ano_construcao,numero, nome, amenidades,status, rua, cidade, estado, cep})
    .then(() => {
      alert("Condomínio cadastrado")
    }).catch(error => {
      if (error.response){
        alert(error.response.data.message)
      }else{
        alert("Não foi possível cadastrar")
      }
    })
  }
  //estados para armazenar informações de endereço
  const [ufs, setUfs] = useState([])
  const [id, setId] = useState(11)
  const [cities, setCities] = useState([])
  const [acronym, setAcronym] = useState("RO")
  const [dataCep, setDataCep] = useState([])

  //busca os estados sempre que o componente é renderizado
  useEffect(() => {
    //busca os estados na api do ibge
    axios.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
    .then(response => {
      setUfs(response.data)
      console.log(ufs)
    })
  },[])



 
  useEffect(() => {
    //percorre os dados da api procurando pelo nome do estado selecionado pelo usuário, guardando seu id
    const uf = ufs.find(uf => uf.nome === estado);
    if (uf) {
      setId(uf.id);
      
    }
  }, [estado, ufs]);//isso ocorre sempre que o estado e ufs mudam

  useEffect(() => {
     //busca pelos dados de municipios com base no id coletado. ocorre sempre que o id muda
      const fetchCities = async () => {
        const response = await axios.get(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${id}/municipios`);
        setCities(response.data);
    
      };
      fetchCities();
    
  }, [id]);


  
  return(
    <Container>
      <Page>
        <Header>
          <h1>Cadastro de Condomínio</h1>
          <p>Preencha o formulário abaixo para cadastrar um novo condomínio</p>
        </Header>
        <Form>
          
         
          <legend>Informações Gerais</legend>
          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"name"}>Nome</Label>
              <Input 
                width={"30rem"}
                placeholder = "nome do condomínio"
                type = "text"
                id = "name"
                onChange = {e => setNome(e.target.value)}
              />
            </div>
            <div >
              <Label htlmFor={"last_name"}>Quantidade de Imóveis</Label>
                <Input 
                  width={"30rem"}
                  placeholder = "Quantos imóveis?"
                  type = "text"
                  onChange = {e => setQuantidadeImoveis(e.target.value)}
                  />
            </div>
          </InputContainer>
          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"tax"}>Taxa</Label>
              <Input 
                width={"30rem"}
                placeholder = "20%"
                type = "text"
                id = "tax"
                onChange = {e => setTaxa(e.target.value)}
              />
            </div>
            <div >
              <Label htlmFor={"last_name"}>Ano de Construção</Label>
                <Input 
                  width={"30rem"}
                  type = "date"
                  onChange = {e => setAnoConstrução(e.target.value)}
                  />
            </div>
          </InputContainer>
    
          <div>
            <Label htlmFor={""}>Status</Label>
            <Select id="status" name="status" onChange = {e => setStatus(e.target.value)}>
              <option value="Em construção">Em contrução</option>
              <option value="Concluido">Concluido</option>
              <option value="Em renovação">Em renovação</option>
            </Select>
          </div>

          <div className="amenidades">
          <Label htlmFor={"amenidades"}>Amenidades</Label>
          <textarea name="amenidades" id="amenidades"  onChange = {e => setAmenidades(e.target.value)}></textarea>
          </div>
          <legend>Informações de Endereço</legend>
          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"rua"}>Estado</Label>
              <Select onChange={e => setEstado(e.target.value) }>
                {ufs.map((uf) => 
                  <option key={uf.id} value={uf.nome}>{uf.nome}</option>

                  
                )}
              </Select>
            </div>
            <div >
              <Label htlmFor={"City"}>Cidade</Label>
                <Select onChange={e => setCidade(e.target.value)}> 
                  {cities.map((city) => 
                  <option key = {city.id} value={city.nome}>{city.nome}</option>)}
                </Select>
            </div>
          </InputContainer>
          <InputContainer>
            <div className="wrapper">
            
              <Label htlmFor={"Rua"}>Rua</Label>
              <Input 
                width={"30rem"}
                placeholder = "Rua das Oliveiras"
                type = "text"
                id = "name"
                onChange = {e => setRua(e.target.value)}
              />
            </div>
            <div >
              <Label htlmFor={"last_name"}>Número da Casa</Label>
                <Input 
                  width={"30rem"}
                  placeholder = "203"
                  type = "number"
                  onChange = {e => setNumero(e.target.value)}
                  />
            </div>
          </InputContainer>
          <div>
            <Label htlmFor={"status"}>CEP</Label>
                <Input 
                  width={"62.2rem"}
                  placeholder = "65213-000"
                  type = "text"
                  id = "CEP"
                  onChange = {e => setCep(e.target.value)}
            
            />
          </div>
          <Button title={"Cadastrar"} onClick = {handleSignUp}/>
        </Form>
      </Page>
 
    </Container>
  )
}