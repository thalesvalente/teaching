import styled from 'styled-components';

export const Container = styled.button`
  width: 100%;

  display: grid;
  grid-template-columns: 50rem auto;
  border: none;
  border-radius: .5rem;
  grid-template-areas:"content image";
  background-color: ${({theme}) => theme.COLORS.WHITE};
  box-shadow: 0px 2px 4px ${({ theme }) => theme.COLORS.BACKGROUND_100};


  

`;

export const Image = styled.img`
  grid-area: image;
  width: 100%;
  height: 26.8rem;
  object-fit: cover;
  border-radius: 5px 5px 0 0;

`

export const AboutProperty = styled.div`
  grid-area: content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 3.5rem 2rem 2rem;
  color: ${({theme})=>theme.COLORS.BACKGROUND_900};

  .titulo {
    margin-top: 1rem;
    text-align: center;
    >p {
      margin-top: 1rem;
      max-width: 40rem;
  
    }
  }  
  .endereco {
    margin-top: 3rem;
  }
  
`
