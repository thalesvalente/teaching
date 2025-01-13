import styled from 'styled-components'

export const Container = styled.div`
  width: 100%;
  height: 100vh;
  
  display: grid;
  grid-template-rows: 10.5rem auto;
  grid-template-areas:
  "header"
  "content" ;

  > main {
    grid-area: content;
    overflow-y: auto;
    padding: 0.4rem 0.8rem;

    color: ${({ theme }) => theme.COLORS.TITLE_100};
  }
`;

export const Header = styled.header`

  grid-area: header;

  height: 6.5rem;
  width: 100%;

  border-bottom-width: 0.1rem;
  border-bottom-style: solid;
  border-color: ${({ theme }) => theme.COLORS.GRAY_100};
  background-color: ${({ theme }) => theme.COLORS.GRAY_100};
 

  display: flex;
  justify-content: space-between;
  
  > a {
    margin-top: 1.6rem;
    svg {
      color: ${({ theme }) => theme.COLORS.TITLE_100};
      font-size: 2.4rem;
    }
  }

  padding: 0 8rem;

`;

export const Logout = styled.button`
  border: none;
  background: none;

  
  svg {
    color: ${({ theme }) => theme.COLORS.TITLE_100};
    font-size: 3.6rem;
  }
  
`;

export const Label = styled.section`

  margin: 1.2rem 0 0;
  padding: 0 6.4rem;

  h2 {
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

export const Content = styled.div`
  max-width: 75rem;
  margin: 0 auto;

  display: flex;
  flex-direction: column;

  > div {

    display: flex;
    align-items: center;

    img {
      width: 100%;
      height: 35rem;
      border-radius: 5%;
      margin: 0;
    }
  }

  dl {
    margin: 0.4rem 0 0.4rem;
    width: 100%;
    padding: 2rem;
    background-color:${({ theme }) => theme.COLORS.BACKGROUND_200} ;
    border-radius: 0.5rem;
    text-align: left;
    dt {
      color: ${({ theme }) => theme.COLORS.TITLE_100};
      font-size: 2rem;
      margin-bottom: 0.5rem
    }

    dd {
      color: ${({ theme }) => theme.COLORS.TEXT};
      font-weight: 600;
      margin-bottom: 1rem;
      border-bottom: 0.1rem solid #ccc
    }
  }

  section {

    margin: 1.2rem 0 0;

    h2 {
      border-bottom-width: 0.1rem;
      border-bottom-style: solid;
      border-bottom-color: ${({ theme }) => theme.COLORS.BACKGROUND_700};

      padding-bottom: 1.6rem;
      margin-bottom: 2.8rem;

      color: ${({ theme }) => theme.COLORS.TEXT};
      font-size: 2.0rem;
      font-weight:  400;
    }
  }

  .buttons {
    width: 50%;

    display: flex;
    gap: 0.8rem;

    margin: 0 auto 0.4rem;
  }

`;
