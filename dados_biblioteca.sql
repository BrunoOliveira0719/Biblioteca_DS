USE Biblioteca_CG
GO

CREATE TABLE Autenticacao_responsavel(
	usuario_responsavel VARCHAR(20),
	senha_responsavel int
	)

CREATE TABLE Autenticacao_ADM(
	usuario_adm VARCHAR(20),
	senha_adm int
	)

CREATE TABLE Livros_existentes(
	livro VARCHAR(6000),
	cod_barra int
	)

CREATE TABLE Livros_retirados(
	Nome_do_aluno VARCHAR(1000),
    RA INT,
    livro VARCHAR(6000),
    cod_barra int,
    data_retirada VARCHAR(15),
    data_entrega VARCHAR(15)
	)

INSERT INTO Autenticacao_ADM(usuario_adm, senha_adm)
VALUES
  ('Bruno_codigos', 12345)
INSERT INTO Autenticacao_ADM(usuario_adm, senha_adm)
VALUES
  ('Prof_Henderson', 123)
INSERT INTO Autenticacao_ADM(usuario_adm, senha_adm)
VALUES
  ('JP_Menino', 123456)

SELECT * FROM Autenticacao_ADM
SELECT * FROM Autenticacao_responsavel
SELECT * FROM Livros_existentes
SELECT * FROM Livros_retirados
