import styled from "styled-components";

export const Container = styled.span`

  font-size: 1.2rem;
  margin-right: 0.6rem;
  color: ${({ theme }) => theme.COLORS.WHITE};
  
  .status-red {
    width: 100%;
    padding: 0.5rem 1.4rem;
    background-color: ${({ theme }) => theme.COLORS.RED };
    border-radius: 0.5rem;
  }
   
  .status-green {
    width: 100%;
    padding: 0.5rem 1.4rem;
    background-color: green;
    border-radius: 0.5rem;
  }

`;

