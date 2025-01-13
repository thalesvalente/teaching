import { Link } from 'react-router-dom';

import { Container } from './styles'

export function ButtonText ({title, to="#", isActive = false , onClick, ...rest}) {
  return (
    <Container 
      type="button"
      $isactive={isActive.toString()}
      onClick={onClick}
      {...rest}
    >
      <Link to={to}>{ title }</Link>
    </Container>
  )
}
