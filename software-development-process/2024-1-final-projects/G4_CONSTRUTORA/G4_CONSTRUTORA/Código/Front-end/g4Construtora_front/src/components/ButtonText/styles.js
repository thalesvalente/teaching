import styled from 'styled-components'

export const Container = styled.button`

  background: none;
  > a {
    color: ${({ theme, $isactive }) => $isactive ? theme.COLORS.TITLE_100 : theme.COLORS.TITLE_200};
  }

  border: none;
  
  font-size: 1.6rem;
`;
