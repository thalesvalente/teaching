import styled from 'styled-components'

export const Container = styled.section`

  margin: 2.8rem 0;

  > h2 {
    border-bottom-width: 0.1rem;
    border-bottom-style: solid;
    border-bottom-color: ${({ theme }) => theme.COLORS.BACKGROUND_700};

    padding-bottom: 1.6rem;
    margin-bottom: 2.8rem;

    color: ${({ theme }) => theme.COLORS.TEXT};
    font-size: 2.0rem;
    font-weight:  400;
  }
`;
