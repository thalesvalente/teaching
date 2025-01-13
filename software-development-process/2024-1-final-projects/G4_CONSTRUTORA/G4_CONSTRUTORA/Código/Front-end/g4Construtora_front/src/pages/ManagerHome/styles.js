import { Link } from 'react-router-dom';
import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  height: 100vh;

  display: grid;
  grid-template-columns: 25rem auto;
  grid-template-rows: 6.5rem 15.8rem 10.8rem auto 6.4rem 6.4rem 6.4rem;
  grid-template-areas:
  "brand header"
  "menu search"
  "menu label"
  "menu content"
  "cond content"
  "createEmployee content"
  "create content"
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
  justify-content: right;
  align-items: center;

  padding: 0 8rem;

`;
 
export const Logout = styled.button`
  border: none;
  background: none;

  > svg {
    color: ${({ theme }) => theme.COLORS.TITLE_100};
    font-size: 3.6rem;
  }
`;

export const Brand = styled.div`
  grid-area: brand;

  display: flex;
  justify-content: center;
  align-items: center;

  border-bottom-width: 0.1rem;
  border-bottom-style: solid;
  border-color: ${({ theme }) => theme.COLORS.GRAY_300};

  background-color: ${({ theme }) => theme.COLORS.GRAY_300};

  > h2 {
    font-size: 5rem;
    color: ${({ theme }) => theme.COLORS.TITLE_100};
  }
`;

export const Menu = styled.ul`
  grid-area: menu;
  background-color: ${({ theme }) => theme.COLORS.GRAY_100};

  padding-top: 16rem;
  text-align: center;

  > li {
    margin-bottom: 2.4rem;
  }

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
  grid-area: content;
  padding: 0 6.4rem;
  overflow-y: auto;

  dl {
    width: 100%;
    padding: 2rem;
    background-color:${({theme}) => theme.COLORS.BACKGROUND_200} ;
    border-radius: 0.5rem;
    text-align: left;
    dt {
      color: ${({theme}) => theme.COLORS.TITLE_100};
      font-size: 2rem;
      margin-bottom: 0.5rem
    }

    dd {
      color: ${({theme}) => theme.COLORS.TEXT};
      font-weight: 600;
      margin-bottom: 1rem;
      border-bottom: 0.1rem solid #ccc
    } 
  }
`;

export const Create = styled(Link)`
  grid-area: create;

  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200 };
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: 1px solid ${({ theme }) => theme.COLORS.GRAY_100};
  border-radius:0 0.5rem 0 0;

  display: flex;
  align-items: center;
  justify-content: center;

  svg {
    margin-right: 0.8rem;
  }

`;

export const Cond = styled(Link)`
  grid-area: cond;

  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200 };
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: 1px solid ${({ theme }) => theme.COLORS.GRAY_100};
  border-radius:0 0.5rem 0 0;

  display: flex;
  align-items: center;
  justify-content: center;

  svg {
    margin-right: 0.8rem;
  }

`;


export const CreateEmployee = styled(Link)`
  grid-area: createEmployee;

  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200 };
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: 1px solid ${({ theme }) => theme.COLORS.GRAY_100};
  border-radius:0 0.5rem 0 0;

  display: flex;
  align-items: center;
  justify-content: center;

  svg {
    margin-right: 0.8rem;
  }
`;

export const Avatar = styled.div`
  grid-area: search;
  display: flex;
  align-items: center;

  padding: 6.4rem 6.4rem 0;

  > img {
    width: 12.8rem;
    height: 12.8rem;
    border-radius: 10%;
  }

  > div {
    display: flex;
    flex-direction: column;
    margin-left: 1.6rem;
    line-height: 2.4rem;

    span {
      font-size: 1.4rem;
      color: ${({ theme }) => theme.COLORS.TEXT};
    }

    strong {
      font-size: 1.8rem;
      color: ${({ theme }) => theme.COLORS.TITLE_100};
    }
  }
`;
