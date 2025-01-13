import styled from "styled-components";


export const Container = styled.div`
  &::before {
    content: "";
    background: ${({ theme }) => theme.COLORS.GRAY_300};;
    display: block;
    width: 100%;
    height: 43.6rem;
    position: absolute;
   z-index: -1;
  }
   
`
export const Page = styled.div`
  width: 75rem;
  margin: 0 auto 30rem;
  padding-top: 13rem;
  margin-bottom: 30rem;
`
export const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 3.2rem;
  min-height: 40rem;
  border-radius: 20px 20px 20px 20px;
  background: #FFF;
  padding: 6.4rem; 
  background-color: ${({theme}) => theme.COLORS.BACKGROUND_300};
  
  >legend {
    color: ${({theme}) => theme.COLORS.TITLE_100};
    font-size: 2.4rem;
    line-height: 3.4rem;
    width: 100%;
    border-bottom: 1px solid #E6E6F0;
    padding-bottom: 1.6rem;
  }

  >h2 {
    font-size: 24px;
    margin: 48px 0;
    margin-bottom: 24px;
    color: ${({theme}) => theme.COLORS.TITLE_200};
    text-align: center;
  }

  >a {
    margin-top: 50px;
  
  }

`

export const InputContainer = styled.div`
  display: flex;
  gap: 2.2rem;
  margin-bottom: 1.5rem;

  .chooseFiles input[type="file"] {
    opacity: 0;
  
}

`

export const Header = styled.header`
 
  
  >h1 {
    font-size: 3.5rem;
    color: ${({theme}) => theme.COLORS.ORANGE};
  }

  >p {

  font-size: 2rem;
  color: ${({theme}) => theme.COLORS.BACKGROUND_200};
  line-height: normal;
  max-width: 41.7rem;
  margin-bottom: 5.8rem;
  }
`

export const Select = styled.select`
  width: 30rem;
  height: 5.6rem;
  padding: 1.6rem;
  border: 1px solid ${({ theme }) => theme.COLORS.BACKGROUND_200};
  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200};
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: none;
  border-radius: 1rem;
  margin-bottom: .8rem;
  background-image: url();

`;

export const SelectEstado = styled.select`
  width: 62.2rem;
  height: 5.6rem;
  padding: 1.6rem;
  border: 1px solid ${({ theme }) => theme.COLORS.BACKGROUND_200};
  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200};
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: none;
  border-radius: 1rem;
  margin-bottom: .8rem;


`;
