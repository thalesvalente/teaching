import styled from "styled-components";

export const Container = styled.div`
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-rows: 7rem auto;
  grid-template-areas: 
  "header"
  "content";

`
export const Details = styled.div`
position: relative;
  grid-area: content;

  display: flex;
  flex-direction: column;

  >img {
    height: 30.5rem;
    object-fit: cover;
    filter: brightness(0.5)
    
  }

  .NameInformation {
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    text-align: center;
    font-weight: 400;
    p{
      font-size: 1.6rem;
    }

    h2 {
      font-size: 3.5rem;
    }
  }

  .PurchaseBox {
    position: fixed;
    display: flex;
    flex-direction: column;
    right: 2rem;
    top: 30rem;

    width: 28.0rem;
    height: 21.0rem;
    padding: 0 2rem;

    border-radius: 0.5rem;
    background-color: ${({theme}) => theme.COLORS.WHITE};

  
    align-items: center;
    justify-content: center;

    p {
      color:  ${({theme}) => theme.COLORS.TITLE_100};
      margin-bottom: 1.6rem;
    }
  }


`

export const AboutProperty = styled.div`
  padding: 2rem;
  h2 {
    font-size: 4rem;
    color: ${({theme}) => theme.COLORS.TITLE_200};
    margin-bottom: 1.6rem;

  }

  dl {
    width: 30rem;
    background-color:${({theme}) => theme.COLORS.BACKGROUND_200} ;
    border-radius: 0.5rem;
    text-align: center;
    dt {
      color: ${({theme}) => theme.COLORS.TITLE_100};
      font-size: 2rem;
      margin-bottom: 0.5rem
    }

    dd {
      color: ${({theme}) => theme.COLORS.TEXT};
      font-weight: 600;
      margin-bottom: 1rem;
      border-bottom: 1px solid #ccc
    }
  }
`
