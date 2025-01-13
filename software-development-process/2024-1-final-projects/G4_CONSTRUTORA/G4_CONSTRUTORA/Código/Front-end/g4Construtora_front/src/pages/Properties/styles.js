import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  height: 100vh;

  display: grid;
  grid-template-columns: auto;
  grid-template-rows: 6.5rem 12.8rem 9.8rem auto;
  grid-template-areas:
  "header"
  "search"
  "label"
  "content"
  ;

  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_100};
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

export const Search = styled.div`
  grid-area: search;
  padding: 6.4rem 6.4rem 0;
`;

export const Label = styled.section`
  grid-area: label;

  margin: 2.8rem 0;
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
  display: flex;
  flex-direction: column;
  gap: 2rem;
  grid-area: content;
  padding: 0 6.4rem;
  overflow-y: auto;
`;
