module.exports = {
  parser: '@typescript-eslint/parser', // Define o parser para TypeScript
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended'
  ],
  parserOptions: {
    ecmaVersion: 2020, // Permite a análise de sintaxe moderna do ECMAScript
    sourceType: 'module', // Permite o uso de imports
    ecmaFeatures: {
      jsx: true // Permite a análise de JSX
    }
  },
  settings: {
    react: {
      version: 'detect' // Detecta automaticamente a versão do React
    }
  },
  rules: {
    // Suas regras personalizadas aqui
    // Exemplo:
    // "@typescript-eslint/explicit-module-boundary-types": "off"
  },
  ignorePatterns: ['webpack.config.js'], // Ignora o arquivo de configuração do Webpack
};
