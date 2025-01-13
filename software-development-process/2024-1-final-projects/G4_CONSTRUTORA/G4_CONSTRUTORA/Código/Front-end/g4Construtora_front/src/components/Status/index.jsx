import { Container } from "./styles";

export function Status ( { title, sold, ...rest}) {
  return (
    <Container {...rest}>
      <div className={sold ? "status-green" : "status-red"}>
        {title}
      </div>
    </Container>
  )
}
