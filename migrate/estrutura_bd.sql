CREATE DATABASE IF NOT EXISTS NaclMusic;

USE NaclMusic;

CREATE TABLE IF NOT EXISTS genero (
 nome_genero VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero (nome_genero)
);
 
drop database NaclMusic;

select * from musica;