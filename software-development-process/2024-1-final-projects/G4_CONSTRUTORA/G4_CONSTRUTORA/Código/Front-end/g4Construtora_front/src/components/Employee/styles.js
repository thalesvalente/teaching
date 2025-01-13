import styled from 'styled-components';

export const Container = styled.button`
  width: 100%;
  border: none;
  border-radius: 1rem;

  padding: 2.2rem;
  margin-bottom: 1.6rem;

  .titulo {
  
    h1 {
      flex: 1;
      text-align: left;
      font-weight: 700;
      font-size: 2.4rem;
      color: ${({ theme }) => theme.TITLE_100};
      margin-bottom: 0.5rem;
    }

    h2 {
      margin-bottom: 0.5rem;
      text-align: left;
      font-weight: 500;
      font-size: 1.6rem;
      color: ${({ theme }) => theme.TITLE_100};
    }

    h3 {
      text-align: left;
      font-weight: 400;
      font-size: 1.6rem;
      color: ${({ theme }) => theme.TITLE_100};
    }
  
    h4 {
      width: 40%;
      margin-top: 1.2rem;
  
      text-align: left;
      font-size: 1.6rem;
      color: ${({ theme }) => theme.COLORS.TITLE_100};
    }
  }

  > footer {
    width: 100%;
    display: flex;
    margin-top: 2.4rem;

    span {
      font-size: 1.2rem;
      margin-right: 0.6rem;
      color: ${({ theme }) => theme.COLORS.WHITE};
  
      padding: 0.5rem 1.4rem;
      background-color: ${({ theme }) => theme.COLORS.GRAY_100};
      border-radius: 0.5rem;
    }

  }

`;
