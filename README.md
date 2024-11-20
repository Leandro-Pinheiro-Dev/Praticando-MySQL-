
# Sistema de Doação de Tintas

## Visão Geral
O **Sistema de Doação de Tintas** foi desenvolvido para promover a sustentabilidade, permitindo que tintas excedentes sejam doadas a instituições e indivíduos que necessitam delas. O sistema conecta doadores e beneficiários, criando uma rede de reutilização de recursos.

## Estrutura do Projeto
O projeto é dividido em três principais componentes:

- **Front-end**: Desenvolvido com HTML, CSS e JavaScript, fornecendo uma interface amigável e responsiva.
- **Back-end**: Implementado em Python com Flask, gerenciando a lógica do sistema e a comunicação com o banco de dados.
- **Banco de Dados**: MySQL é utilizado para armazenar e gerenciar todas as informações do sistema.

## Funcionalidades Principais
- **Registro e Autenticação de Usuários**: Cadastro seguro de doadores e beneficiários, com validação de email e senha.
- **Gestão de Doações**: Registro, edição e exclusão de doações, incluindo detalhes como tipo de tinta, cor, quantidade e validade.
- **Solicitação de Tintas**: Beneficiários podem procurar e solicitar tintas com base em suas preferências.
- **Painel de Controle**: Fornece estatísticas sobre o número de tintas doadas, beneficiários e dados de interação.

## Tecnologias Utilizadas
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Banco de Dados**: MySQL
- **IDE**: Visual Studio Code (VS Code)
- **Ferramentas Adicionais**: Postman para testes de API, MySQL Workbench para visualização de dados

## Estrutura do Banco de Dados
O banco de dados foi projetado para armazenar informações de usuários, doadores, beneficiários, e estatísticas gerais.

### Script Completo de Banco de Dados (DDL)

```sql
-- Criação da base de dados
CREATE DATABASE DBteste;
USE DBteste;

-- Tabela de usuários
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    cidade VARCHAR(50),
    senha VARCHAR(255)
);

-- Tabela de login
CREATE TABLE login (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    senha VARCHAR(255),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabela de beneficiados
CREATE TABLE beneficiado (
    id_beneficiado INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    data_retirada DATE,
    observacao TEXT,
    tinta VARCHAR(50),
    cor VARCHAR(50)
);

-- Tabela de doadores
CREATE TABLE doador (
    id_doador INT PRIMARY KEY AUTO_INCREMENT,
    nome_doador VARCHAR(100),
    tipo_tinta VARCHAR(50),
    cor VARCHAR(50),
    acabamento VARCHAR(50),
    quantidade INT,
    validade DATE,
    condicao VARCHAR(50)
);

-- Tabela de dashboard
CREATE TABLE dashboard (
    id_dashboard INT PRIMARY KEY AUTO_INCREMENT,
    data_pesquisa DATE,
    fatur_vendas DECIMAL(10, 2),
    tintas_doadas INT,
    apple INT,
    facebook INT,
    twitter INT,
    paypal INT
);

-- Criação de usuário e permissões
CREATE USER 'BDteste'@'localhost' IDENTIFIED BY '461663';
GRANT ALL PRIVILEGES ON DBteste.* TO 'BDteste'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'BDteste'@'localhost';
```

## Configuração e Instalação

### Pré-requisitos
- **Python**
- **MySQL Server**
- **Visual Studio Code** (ou qualquer editor de código de sua preferência)
- **Postman** (opcional para testes de API)

### Passos de Instalação
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows, use `env\Scripts\activate`
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:
   - Importe o script DDL fornecido no MySQL Workbench ou em seu gerenciador de banco de dados preferido.

5. **Configure as variáveis de ambiente**:
   - Crie um arquivo `.env` e adicione as credenciais do banco de dados:
     ```env
     DB_HOST=localhost
     DB_USER=BDteste
     DB_PASSWORD= Sua_Senha
     DB_NAME=DBteste
     ```

6. **Inicie o servidor Flask**:
   ```bash
   flask run
   ```

7. **Acesse a aplicação**:
   - Navegue até `http://127.0.0.1:5000/` no seu navegador.


## Contribuição
Contribuições são bem-vindas! Para contribuir, siga os seguintes passos:
1. Faça um fork do projeto.
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Faça o commit das alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
