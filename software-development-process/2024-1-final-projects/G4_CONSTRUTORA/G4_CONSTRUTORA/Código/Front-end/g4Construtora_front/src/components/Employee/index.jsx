import { Container} from './styles';
//Este componente exibe informações de um funcionário. Os dados do funcionário
export function Employee({ data, ...rest }) {
  return (
    <Container {...rest}>
      <div className='titulo'>

        <h1>{data.nome}</h1>
        <h2>ID : {data.id}</h2>
        <h3>Tempo de contrato: {data.tempocontrato}</h3>
        <h4>Carga Horaria : {data.cargaHoraria}</h4>

      </div>

      <footer>
        <span>{data.cargo}</span>
      </footer>

    </Container>
  )
}
