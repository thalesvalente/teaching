import styled from 'styled-components'

export const Container = styled.header`

  grid-area: header;

  height: 7rem;
  width: 100%;

  border-bottom-width: 0.1rem;
  border-bottom-style: solid;
  background-color: ${({ theme }) => theme.COLORS.WHITE};
 

  display: flex;
  position: relative;
  align-items: center;

  padding: 0 8rem;

  > h2 {
    position: absolute;
    left: 3rem;
    font-size: 5rem;
    color: ${({ theme }) => theme.COLORS.TITLE_100};
  }
nav {
  position: absolute;
  right: 25rem;
  > ul {
    list-style: none;
    font-size: 2rem;
  
    li {
      display: inline-block;
      position: relative;

      &:hover .DropDown { /* Exibe o dropdown no hover */
        display: block;
      }
        
      .DropDown { /* Sem o ul que envolvia o .Dropdown */
        position: absolute;
        width: 20rem;
        background-color: ${({ theme }) => theme.COLORS.WHITE};
        border-radius: 1rem;
        padding: 1rem;
        display: none; /* Oculta o dropdown por padrão */
        z-index: 999;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        border: 1px solid ${({theme}) => theme.COLORS.GRAY_300};
      

        li {
          display: block;
          margin-bottom: 1.5rem;
        }
      }

      a {
        display: block;
        color: black;
        text-decoration: none;
        text-align: center;
        padding: 0 2rem;
        color:  ${({ theme }) => theme.COLORS.TEXT_100 };
      }
    }
  }
}

`;



  




  
   

 
export const Logout = styled.button`
  position: absolute;
  right: 2rem;
  border: none;
  background: none;

  > svg {
    color: ${({ theme }) => theme.COLORS.GRAY_100};
    font-size: 3.6rem;
  }
`;
