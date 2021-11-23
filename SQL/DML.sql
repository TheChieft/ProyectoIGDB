
/* 
Porfavor cambie SQL\database\DB_Homicidios.csv y SQL\database\DB_Departamentos_y_municipios_de_Colombia.csv
en el codigo, ponga su ruta donde descargo la base de datos DB_departamento y DB_homicidios 
un ejemplo : "C:\Users\USER\Downloads" 
*/
COPY PUBLIC.datos_no_normalizado FROM 'SQL\database\DB_Homicidios.csv'DELIMITER ',' CSV HEADER;

COPY PUBLIC.tabla_municipios_departamentos FROM 'SQL\database\DB_Departamentos_y_municipios_de_Colombia.csv'DELIMITER ';' CSV HEADER;

UPDATE tabla_municipios_departamentos set Region = Upper(Region), Departamento = Upper(Departamento), Municipio = Upper(Municipio);


INSERT INTO departamento( 
	SELECT DISTINCT md.Codigo_Dane_Departamento, md.Departamento
	FROM tabla_municipios_departamentos AS md);
	
INSERT INTO municipio(
	SELECT md.Codigo_Dane_Municipio, md.Municipio, md.Codigo_Dane_Departamento
	FROM tabla_municipios_departamentos md
);

INSERT INTO tipo_arma(Nombre_arma)
	SELECT DISTINCT dnn.Arma_Medio
	FROM datos_no_normalizado dnn;
	
INSERT INTO genero_victimario(Nombre_genero)
	SELECT DISTINCT dnn.Genero_Victimario
	FROM datos_no_normalizado dnn;

INSERT INTO grupo_etario(Nombre_grupo_etario)
	SELECT DISTINCT dnn.Grupo_Etario_Victimario
	FROM datos_no_normalizado dnn;
	
INSERT INTO tipo_homicidio(Nombre_tipo_homicidio)
	SELECT DISTINCT dnn.Descripcion
	FROM datos_no_normalizado dnn;
	
INSERT INTO homicidios_colombia(Fecha_homicidio,Numero_Victimas,ID_tipo_homicidio,ID_tipo_arma,
			ID_genero_victimario,ID_grupo_etario_victimario,Codigo_Dane_municipio)
	SELECT dnn.Fecha_Hecho, dnn.Cantidad_Victimas, th.ID_tipo_homicidio,ta.ID_tipo_arma,
	gv.ID_genero_victimario,ge.ID_grupo_etario,m.Codigo_Municipio_Dane
	FROM datos_no_normalizado dnn, tipo_homicidio th, tipo_arma ta, genero_victimario gv, grupo_etario ge, municipio m
	WHERE th.Nombre_tipo_homicidio = dnn.Descripcion AND ta.Nombre_arma = dnn.Arma_Medio AND gv.Nombre_genero=dnn.Genero_Victimario
		AND ge.Nombre_grupo_etario = dnn.Grupo_Etario_Victimario AND m.Nombre_Muncipio = dnn.Municipio;
		
DROP TABLE datos_no_normalizado;
DROP TABLE tabla_municipios_departamentos;
