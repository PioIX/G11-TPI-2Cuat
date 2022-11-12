que CREATE TABLE IF NOT EXISTS'Chefs' (
	'id_chef'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'usuario'	TEXT NOT NULL,
	'contra'	TEXT NOT NULL
  );

CREATE TABLE IF NOT EXISTS'Recetas' ( -- agregar forma de relacion con los ingredientes
	'id_receta'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	'nombre'	TEXT NOT NULL,
	'descripcion'	TEXT NOT NULL,
	'pais_origen'	TEXT,
	'img'	INTEGER,
	'id_chef'	INTEGER NOT NULL,
	FOREIGN KEY('id_chef') REFERENCES 'Chefs' ('id_chef')
  );

CREATE TABLE IF NOT EXISTS'Ingredientes' (
	'id_ingrediente'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'nombre'	TEXT NOT NULL
  );

CREATE TABLE IF NOT EXISTS 'Lista_ingredientes' (
	'id_ingrediente'	INTEGER, 
	'id_receta'	INTEGER, 
	FOREIGN KEY('id_ingrediente') REFERENCES Ingredientes ('id_ingrediente'),
  FOREIGN KEY('id_receta') REFERENCES Recetas ('id_receta')
  );

-- INSERT INTO 'Chefs' VALUES (1, 'admin', '123G11');
-- INSERT INTO 'Ingredientes' VALUES (1, 'aceite');
-- INSERT INTO 'Ingredientes' VALUES (2, 'papa');
-- INSERT INTO 'Recetas' VALUES (1, 'Papas fritas', 'Fritar las papas en el aceite', 'Argentina', 1, 1);
-- INSERT INTO 'Lista_ingredientes' VALUES (1, 1);
COMMIT;

