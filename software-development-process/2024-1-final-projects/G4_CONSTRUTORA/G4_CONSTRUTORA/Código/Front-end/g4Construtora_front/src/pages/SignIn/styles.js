import styled from 'styled-components';
import backgroundImg from '../../assets/background.jpeg';

export const Container = styled.div`
  height: 100vh;

  display: flex;
  align-items: stretch;

`;

export const Form = styled.form`
  padding: 0 13.6rem;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  text-align: center;

  > h1 {
    font-size: 4.8rem;
    color: ${({ theme }) => theme.COLORS.TITLE_100};
  }

  > h2 {
    font-size: 2.4rem;
    margin: 4.8rem 0;
    color: ${({ theme }) => theme.COLORS.TITLE_200}
  }

  > p {
    font-size: 1.4rem;
    color: ${({ theme }) => theme.COLORS.TITLE_200}
  }

  > a {
    margin-top: 12.4rem;
    color: ${({ theme }) => theme.COLORS.TITLE_100};


  }

  .label {
    margin-right: 42.5rem;
  }

`;

export const Background = styled.div`
  flex: 1;
  background: url(${backgroundImg}) no-repeat center center;
  background-size: cover;
`;
