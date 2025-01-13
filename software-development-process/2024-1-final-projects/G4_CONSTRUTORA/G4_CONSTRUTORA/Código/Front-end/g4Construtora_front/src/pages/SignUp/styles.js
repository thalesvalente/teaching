import styled from "styled-components";
import Background from "../../assets/background.jpeg"

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

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 3.2rem;
  min-height: 40rem;
  border-radius: 20px 20px 20px 20px;
  background: #FFF;
  padding: 1rem 6.4rem 6.4rem; 
  background-color: ${({theme}) => theme.COLORS.BACKGROUND_300};
  

  >h2 {
    font-size: 24px;
    margin-top: 24px;
    color: ${({theme}) => theme.COLORS.TITLE_200};
    align-self: center;
  }

  >a {
    margin-top: 50px;
  
  }

`

export const InputContainer = styled.div`
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1.5rem;

`

export const BackgroundImg = styled.div`
  flex : 1;
  background: url(${Background}) no-repeat center center;
  background-size: cover;
`

export const Select = styled.select`
  width: 30rem;
  height: 5.6rem;
  padding: 1.6rem;
  border: 1px solid ${({ theme }) => theme.COLORS.BACKGROUND_200};
  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200};
  color: ${({ theme }) => theme.COLORS.TEXT_200};
  border: none;
  border-radius: 1rem;
  margin-bottom: .8rem;
  background-image: url();

`;

export const Page = styled.div`
  width: 75rem;
  margin: 0 auto 15rem;
  padding-top: 15rem;
`


export const Header = styled.header`
  width: 100%;
  background-color: ${({ theme }) => theme.COLORS.GRAY_300};
  padding: 20px;
  z-index: 10; 
  align-items: center;
  text-align: center;
  
  >h1 {
    font-size: 3.5rem;
    color: ${({theme}) => theme.COLORS.WHITE};
  }

  >p {
    font-size: 1.4rem;
    color: ${({theme}) => theme.COLORS.TITLE_WHITE}
  }
`










