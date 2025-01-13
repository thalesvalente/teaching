import { createContext, useContext, useEffect } from "react";
import { useState } from "react";
import { api } from "../services/api";

// Cria um contexto de autenticação com valor padrão vazio
const AuthContext = createContext({})
// Define um provedor de autenticação que encapsula a lógica de autenticação e fornece contexto para seus filhos
function AuthProvider({children}){
  // Define o estado inicial com dados vazios
   const [data,setData] = useState("")
   // Função para realizar o login do usuário
  async function signIn({cpf,password}){
    try {
      // Faz uma requisição de login à API com o CPF e a senha fornecidos
      const response = await api.post("/Login", {cpf, password})
        const {sucesso} = response.data
        // Atualiza o estado local com os dados de sucesso recebidos
        setData({sucesso})
        // Armazena os dados de sucesso no localStorage para persistência de sessão
        localStorage.setItem("@g4construtora : sucesso", JSON.stringify(sucesso))
      
    } catch (error) {
      if(error.response){
        alert(error.response.data.message)
      }else{
        alert("não foi possivel entrar")
      }
    }
    

  }
  // Função para realizar o logout do usuário
  function signOut(){
    // Remove os dados de sucesso do localStorage
    localStorage.removeItem("@g4construtora : sucesso")
   // Atualiza o estado local para um estado vazio, indicando que o usuário saiu
    setData({})
  }
  // useEffect para recuperar dados de autenticação do localStorage quando o componente é montado
  useEffect(() => {
    const sucesso = localStorage.getItem("@g4construtora : sucesso")
    if (sucesso){
      setData({
        sucesso :JSON.parse(sucesso)// Atualiza o estado local com os dados persistidos
      })
    }
  },[])
  // Provedor de contexto que disponibiliza as funções e dados de autenticação para os componentes filhos
  return(
    <AuthContext.Provider value ={{signIn,user : data.sucesso,signOut}}>
      {children}
    </AuthContext.Provider>
  )

}

// Hook personalizado para acessar o contexto de autenticação
  function useAuth(){
    // Retorna o contexto de autenticação para uso nos componentes
    const context = useContext(AuthContext)

    return context
  }
// Exporta o provedor de autenticação e o hook personalizado
export {AuthProvider, useAuth }