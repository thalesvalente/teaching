import { FiArrowLeft, FiUser, FiCamera, FiDollarSign } from 'react-icons/fi';
import { FaUserTie, FaRegClock } from 'react-icons/fa';
import { MdDateRange } from 'react-icons/md';
import { IoIosArrowDown } from 'react-icons/io';

import { Button } from '../../components/Button';
import { Label } from '../../components/Label';
import { Input } from '../../components/Input';
import { api } from '../../services/api';
import { useState } from 'react';

import { Container, Form, Avatar, Select } from './styles';

export function CreateEmployee() {


  //estados para armazenar os dados do form
  const [nome,setNome] = useState("")
  const [cpf,setCpf] = useState("")
  const [nFilhos,setFilhos] = useState("")
  const [estado_civil, setEstadoCivil] = useState("")
  const [recebe_renda, setRenda] = useState("")
  const [funcao, setFuncao] = useState("")
  const [data_pagamento,setPagamento] = useState("")
  const [cargaHoraria, setCargaHoraria] = useState("")


  function HandleCreateEmployee(){
    //verifica se todos os dados forma inseridos
    if (!nome || !cpf || !nFilhos || !estado_civil || !recebe_renda || !funcao || !data_pagamento || !cargaHoraria){
      return (alert("Preencha todos os campos"))
    }
    //conversão de string para number
    const numero_de_filhos = Number(nFilhos)
    const renda = Number(recebe_renda)
    const carga_horaria  = Number(cargaHoraria)
    console.log(numero_de_filhos, renda,carga_horaria, nome,cpf,estado_civil, funcao, data_pagamento)

    //envia os dados para a base de dados
    api.post("/funcionario/cadastro", {numero_de_filhos, renda,carga_horaria, nome,cpf,estado_civil, funcao, data_pagamento})
    .then(() => {
      alert("Funcionário cadastrado")
    }).catch(error => {
      if (error.response){
        alert(error.response.data.message)
      }else{
        alert("Não foi possível cadastrar")
      }
    })
  }
  return (
    <Container>

      <header>

        <a href="/">

          <FiArrowLeft />

        </a>

      </header>

      <Form>

        <Avatar>

          <img
            src="https://africancropsciencesociety.org/wp-content/uploads/2020/02/default.jpg"
            alt="Foto do funcionário"
          />

          <label htmlFor="avatar">

            <FiCamera />

            <input
              id="avatar"
              type="file"
            />

          </label>

        </Avatar>

        <Label htmlFor={"name"} className="label">Nome do Funcionário</Label>

        <Input
          placeholder="Nome completo"
          type="text"
          icon={FiUser}
          id="name"
          onChange = {e => setNome(e.target.value)}
        />

        <Label htmlFor={"funcao"} className="label">Função</Label>

       <Select>
        <option value="Corretor">Corretor</option>
        <option value="Interno Geral">Interno Geral</option>
       </Select>

        <Label htmlFor={"cpf"} className="label">Nº do CPF</Label>

        <Input
          placeholder="000.000.000-00"
          type="text"
          id="cpf"
          onChange = {e => setCpf(e.target.value)}
        />

        <Label htmlFor={"cargaHoraria"} className="label">Carga Horária</Label>

        <Input
          type="number"
          icon={FaRegClock}
          id="cargaHoraria"
          onChange = {e => setCargaHoraria(e.target.value)}
        />

        <Label htmlFor={"dataPagamento"} className="label">Data de Pagamento</Label>

        <Input
          type="text"
          icon={MdDateRange}
          id="dataPagamento"
          onChange = {e => setPagamento(e.target.value)}
        />

        <Label htmlFor={"renda"} className="label">Renda Mensal</Label>

        <Input
          placeholder="Renda"
          icon={FiDollarSign}
          type="number"
          id="renda"
          onChange = {e => setRenda(e.target.value)}
        />

        <Label htmlFor={"filhos"} className="label">Nº de Filhos</Label>

        <Input
          placeholder="Digite o número de filhos do contribuinte"
          type="number"
          id="filhos"
          onChange = {e => setFilhos(e.target.value)}
        />

        <Label htlmFor={"estadoCivil"} className="label">Estado Civil</Label>

        <Select id="estadoCivil" name="estadoCivil" onChange = {e => setEstadoCivil(e.target.value)}>
          <option value="solteiro">Solteiro(a)</option>
          <option value="casado">Casado(a)</option>
          <option value="divorciado">Divorciado(a)</option>
          <option value="viuvo">Viúvo(a)</option>
          <IoIosArrowDown />
        </Select>

        <Button title="Salvar" onClick = {HandleCreateEmployee} />

      </Form>

    </Container>
  )
}
