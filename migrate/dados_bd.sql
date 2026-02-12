INSERT INTO `naclmusic`.`genero`
(`nome_genero`,
`icone`,
`cor`)
VALUES
("Metal","","#800000"),
("Rock","","#8B0000"),
("MPB","","#B22222"),
("Pop","","#A52A2A"),
("Funk","","#DC143C")
;
INSERT INTO `naclmusic`.`musica`
(
`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
(
"Avenged Sevenfold",
"08:01",
"A Little Piece Of Heaven",
"https://i.ytimg.com/vi/KVjBCT2Lc94/maxresdefault.jpg",
"Metal"),
(
"Lady Gaga",
"04:15",
"Government Hooker",
"https://i.scdn.co/image/ab67616d0000b273a5d31644260279be8d0c46c0",
"Pop")
;
