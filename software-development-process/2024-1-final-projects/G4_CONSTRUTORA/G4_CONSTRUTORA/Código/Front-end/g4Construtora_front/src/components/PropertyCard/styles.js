import { Link } from "react-router-dom";
import styled from "styled-components";

export const Container = styled(Link)`
  width: 35rem;
  height: 50rem;
  display: grid;
  grid-template-rows: 26.8rem auto;
  border-radius: .5rem;
  grid-template-areas: "image" "content";
  background-color: ${({theme}) => theme.COLORS.WHITE};
  box-shadow: 0px 2px 4px ${({ theme }) => theme.COLORS.BACKGROUND_100}

`

export const Image = styled.img`
  grid-area: image;
  width: 100%;
  height: 26.8rem;
  object-fit: cover;
  border-radius: 5px 5px 0 0;

`

export const AboutProperty = styled.div`
  grid-area: content;
  width: 100%;
  padding: 3.5rem 2rem 2rem;
  color: ${({theme})=>theme.COLORS.BACKGROUND_900};
  position: relative;

  > h1 {
    font-size: 2.6rem;
    margin-bottom: 1rem;
    font-weight: 400;   
    color: ${({ theme }) => theme.COLORS.TITLE_100}; 
    margin-bottom: 0.5rem; 
  }

  > p {
    font-size: 1.4rem;
    font-weight: 400;
    line-height: 1.5;
    color: ${({ theme }) => theme.COLORS.TEXT};
    margin-bottom: 1rem;
  }

  > span {
    font-size: 2rem; 
    font-weight: 700;   
    margin-top: 1.5rem; 
    display: block; 
    position:absolute ;
    bottom: 2.5rem;
    right: 15.2rem;
  }



`