import { FiArrowLeft, FiUser, FiMail, FiLock, FiCamera, FiDollarSign } from 'react-icons/fi';
import { Section } from '../../components/Section';
import { Button } from '../../components/Button';
import { Label } from '../../components/Label';
import { Input } from '../../components/Input';
import { useAuth } from '../../hook/auth';
import { useState } from 'react';
import {Container, Form, Avatar, Select} from './styles';

export function Profile () {
  const {user} = useAuth() // Obtém os dados do usuário autenticado através do hook useAuth
  console.log(user.cpf)

  //estados que armazenam os dados do form
  const [cpf, setCpf] = useState("")
  const [nome, setNome] = useState(user.nome)
  const [numeroDeFilhos, setNumerodeFilhos] = useState(user.numero_de_filhos)
  const [estado_civil, setEstadoCivil] = useState(user.estado_civil)
  const [renda2, setRenda] = useState(user.renda) 
  return (
    <Container>

      <header>

        <a href="/">

          <FiArrowLeft/>
          
        </a>

      </header>

      <Form>

        <Avatar>
          
          <img 
          src="https://github.com/diogobrasil.png" 
          alt="Foto do usuário" 
          />

          <label htmlFor="avatar">
            
            <FiCamera/>

            <input 
            id="avatar"
            type="file" 
            />

          </label>

        </Avatar>

        <Label htmlFor={"name"} className="label">Nome</Label>

        <Input
          placeholder = {user.nome}
          type="text"
          icon={FiUser}
          id="name"
          onChange = {e => setNome(e.target.value)}
        />
      
        <Label htmlFor={"cpf"} className="label">Nº do CPF</Label>

        <Input
          placeholder = {user.cpf}
          type="text"
          id="cpf"
          onChange = {e => setCpf(e.target.value)}
        />

        <Label htmlFor={"renda"} className="label">Renda Mensal</Label>

        <Input
          placeholder = {user.renda}
          icon={FiDollarSign}
          type="number"
          id="renda"
          onChange = {e => setRenda(e.target.value)}
        />

        <Label htmlFor={"filhos"} className="label">Nº de Filhos</Label>

        <Input
          placeholder = {user.numero_de_filhos}
          type="number"
          id="filhos"
          onChange = {e => setNumerodeFilhos(e.target.value)}
        />

        <Label htlmFor={"estadoCivil"} className="label">Estado Civil</Label>
            
        <Select id="estadoCivil" name="estadoCivil"  onChange = {e => setEstadoCivil(e.target.value)}>
          <option value="solteiro">Solteiro(a)</option>
          <option value="casado">Casado(a)</option>
          <option value="divorciado">Divorciado(a)</option>
          <option value="viuvo">Viúvo(a)</option>
        </Select>

        <Section title="Endereço">

        <Label htmlFor={"cep"} className="label">Nº do CEP</Label>

        <Input
          placeholder="00000-000"
          type="number"
          id="cep"
        />
         
        <Label htmlFor={"rua"} className="label">Nome da Rua</Label>

        <Input
          placeholder="Qual o nome da sua rua?"
          type="text"
          id="rua"
        />

        <Label htmlFor={"casa"} className="label">Nº da sua Casa</Label>

        <Input
          placeholder="Qual o número da sua casa?"
          type="number"
          id="casa"
        />

        <Label htmlFor={"bairro"} className="label">Nome do Bairro</Label>

        <Input
          placeholder="Qual o nome do seu bairro?"
          type="text"
          id="bairro"
        />

        <Label htmlFor={"cidade"} className="label">Nome da sua Cidade</Label>

        <Input
          placeholder="Qual o nome da sua cidade?"
          type="text"
          id="cidade"
        />

        </Section>

        <Section title="Sua Senha">

        <Label htmlFor={"senhaAtual"} className="label">Senha Atual</Label>

        <Input
          placeholder="Mín de 6 e Máx de 8 caracteres"
          type="password"
          icon={FiLock}
          id="senhaAtual"
          minLength="6"
          maxLength="8"
        />

        <Label htmlFor={"senhaNova"} className="label">Nova Senha</Label>

        <Input
          placeholder="Mín de 6 e Máx de 8 caracteres"
          type="password"
          icon={FiLock}
          id="senhaNova"
          minLength="6"
          maxLength="8"
        />

        </Section>

        <Button title="Salvar"/>

      </Form>

    </Container>
  )
}
