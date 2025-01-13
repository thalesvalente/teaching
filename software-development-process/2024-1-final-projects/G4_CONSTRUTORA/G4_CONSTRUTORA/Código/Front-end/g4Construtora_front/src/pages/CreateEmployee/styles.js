import styled from 'styled-components';

export const Container = styled.div`
  width: 100%;
  margin-bottom: 1.2rem;

  > header {
    width: 100%;
    height: 14.4rem;

    background-color: ${({ theme }) => theme.COLORS.GRAY_300};

    display: flex;
    align-items: center;

    padding: 0 12.4rem;

    svg {
      color: ${({ theme }) => theme.COLORS.GRAY_100};
      font-size: 2.4rem;
    }
  }

`;

export const Form = styled.form`
  max-width: 75rem;
  margin: 3rem auto 0;

  .label {
    margin-top: 1.6rem;
  }

  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

`;

export const Avatar = styled.div`
  position: relative;
  margin: -12.4rem auto 3.2rem;

  width: 18.6rem;
  height: 18.6rem;

  > img {
    width: 18.6rem;
    height: 18.6rem;
    border-radius: 50%;
  }
  
  > label {
    width: 4.8rem;
    height: 4.8rem;

    background-color: ${({ theme }) => theme.COLORS.GRAY_300};
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    position: absolute;
    bottom: 0.7rem;
    right: 0.7rem;

    cursor: pointer;

    input {
      display: none;
    }

    svg {
      width: 2rem;
      height: 2rem;
      color: ${({ theme }) => theme.COLORS.BACKGROUND_200};
    }
  }
`;

export const Select = styled.select`
  width: 100%;
  height: 5.6rem;
  padding: 1.6rem;
  border: 0.1rem solid ${({ theme }) => theme.COLORS.GRAY_300};
  background-color: ${({ theme }) => theme.COLORS.BACKGROUND_200};
  color: ${({ theme }) => theme.COLORS.TITLE_100};
  border: none;
  border-radius: 1rem;
  margin-bottom: .8rem;
  background-image: url();

  font-family: 'Roboto Slab', sans-serif;
  font-size: 1.6rem;

  > option {
    font-family: 'Roboto Slab', sans-serif;
    font-size: 1.6rem;
  }

`;
