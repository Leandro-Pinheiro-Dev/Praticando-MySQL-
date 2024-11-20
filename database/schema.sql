CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Tipo ENUM('Doador', 'Beneficiário'),
    Endereco VARCHAR(255),
    Cidade VARCHAR(50),
    Estado CHAR(2),
    CEP VARCHAR(10),
    Email VARCHAR(100),
    Telefone VARCHAR(15),
    Justificativa TEXT
);

CREATE TABLE Tinta (
    ID_Tinta INT AUTO_INCREMENT PRIMARY KEY,
    Tipo VARCHAR(50),
    Cor VARCHAR(50),
    Acabamento VARCHAR(50),
    Quantidade INT,
    Validade DATE,
    Foto VARCHAR(255),
    Condicao VARCHAR(20)
);

CREATE TABLE Estoque (
    ID_Estoque INT AUTO_INCREMENT PRIMARY KEY,
    ID_Tinta INT,
    Quantidade_Disponivel INT,
    FOREIGN KEY (ID_Tinta) REFERENCES Tinta(ID_Tinta)
);

CREATE TABLE Doacao (
    ID_Doacao INT AUTO_INCREMENT PRIMARY KEY,
    Data DATE,
    Status ENUM('Aprovada', 'Rejeitada', 'Parcial'),
    Local_Doacao VARCHAR(50),
    ID_Usuario INT,
    ID_Tinta INT,
    Observacao TEXT,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Tinta) REFERENCES Tinta(ID_Tinta)
);

CREATE TABLE Pedido (
    ID_Pedido INT AUTO_INCREMENT PRIMARY KEY,
    Data DATE,
    Status ENUM('Aprovado', 'Parcial', 'Rejeitado'),
    ID_Usuario INT,
    ID_Tinta INT,
    Quantidade_Solicitada INT,
    Justificativa TEXT,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Tinta) REFERENCES Tinta(ID_Tinta)
);
