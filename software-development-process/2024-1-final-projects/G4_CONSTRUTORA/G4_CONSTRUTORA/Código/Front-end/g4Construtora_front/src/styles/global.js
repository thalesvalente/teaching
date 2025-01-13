import { createGlobalStyle } from "styled-components";

// Define estilos globais para a aplicação
export default createGlobalStyle`
  :root {
    font-size: 62.5%;
  }
  
 * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
 }

 body {
  background-color: ${({theme}) => theme.COLORS.BACKGROUND_100};
  color: ${({theme}) => theme.COLORS.WHITE};
  -webkit-font-smoothing : antialised
 }
 body, button, textarea,input {
  font-family: "Roboto Slab", serif;
  font-size: 1.6rem;
  outline: none;

 }

 a {
  text-decoration: none;
 }

 a, button {
  cursor: pointer;
 transition: filter 0.2s;
 }

 a:hover, button:hover {
  filter: brightness(0.9);
 }
`
