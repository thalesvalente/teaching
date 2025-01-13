import React from 'react';
import ReactDOM from 'react-dom/client';
import { ThemeProvider} from 'styled-components';
import theme from './styles/theme';
import GlobalStyle from "./styles/global";
import { Routes } from './routes';
import { AuthProvider } from './hook/auth';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <GlobalStyle/>
      <AuthProvider>
         <Routes/>
      </AuthProvider>
    </ThemeProvider>
  </React.StrictMode>,
)
