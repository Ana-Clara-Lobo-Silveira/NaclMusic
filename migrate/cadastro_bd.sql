CREATE TABLE IF NOT EXISTS cadastro(
usuario VARCHAR(20) NOT NULL PRIMARY KEY,
senha VARCHAR(100) NOT NULL
);



select * from cadastro where usuario = "a";