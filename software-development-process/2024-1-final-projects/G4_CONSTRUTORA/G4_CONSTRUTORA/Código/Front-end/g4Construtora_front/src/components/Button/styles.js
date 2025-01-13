import styled from "styled-components";

export const Container = styled.button`
  width: 100%;
  background-color: ${({theme}) => theme.COLORS.GRAY_300};
  color: ${({theme}) => theme.COLORS.WHITE};

  height: 56px;
  border: none;
  padding: 16px;
  margin-top: 16px;
  border-radius: 10px;
  font-weight: 500;

  & :disabled {
    opacity: 0.5;
  }
  
`
