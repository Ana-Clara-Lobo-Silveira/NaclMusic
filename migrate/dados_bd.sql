INSERT INTO `naclmusic`.`genero`
(`nome_genero`,
`icone`,
`cor`)
VALUES
("Metal","","#800000"),
("Rock","","#8B0000"),
("MPB","","#B22222"),
("Pop","","#A52A2A"),
("Funk","","#DC143C"),
("Eletronica", "", "#DC143c"),
("Hip-Hop", "", "#DC143c")
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
"Pop"),
(
"6arelyhuman",
"02:04",
"Faster n Harder",
"https://cdn-images.dzcdn.net/images/cover/cb5d123032833ff44a3abee8d234ff93/0x1900-000000-80-0-0.jpg",
"Eletronica"),
(
"System Of A Down",
"02:58",
"Stealing Society",
"https://i.scdn.co/image/ab67616d0000b273a2982eadad9b21912ed6c2e8",
"Metal"),
("System Of A Down",
"04:01",
"Forest",
"https://images.genius.com/c0aaba396a081250ebe9c5809ddaab60.1000x1000x1.png",
"Metal"),
("Yago Oproprio",
"03:31",
"Papoulas",
"https://i.scdn.co/image/ab67616d0000b2738855874e76e6747c529c49fb",
"Hip-Hop")
;

