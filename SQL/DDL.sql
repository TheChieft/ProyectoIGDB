CREATE TABLE PUBLIC.datos_no_normalizado(
	Departamento varchar(50) NOT NULL,
	Municipio varchar(50) NOT NULL,
	Codigo_Dane integer NOT NULL,
	Arma_Medio varchar(50) NOT NULL,
	Fecha_Hecho date NOT NULL,
	Genero_Victimario varchar(50) NOT NULL,
	Grupo_Etario_Victimario varchar(50) NOT NULL,
	Descripcion varchar(50) NOT NULL,
	Cantidad_Victimas smallint NOT NULL
);

CREATE TABLE PUBLIC.tabla_municipios_departamentos(
	Region varchar(100) NOT NULL,
	Codigo_Dane_Departamento integer NOT NULL,
	Departamento varchar(100) NOT NULL,
	Codigo_Dane_Municipio integer NOT NULL,
	Municipio varchar(100) NOT NULL
);

COPY PUBLIC.datos_no_normalizado FROM 'SQL\database\DB_Departamentos_y_municipios_de_Colombia.csv' DELIMITER ',' CSV HEADER;

COPY PUBLIC.tabla_municipios_departamentos FROM 'SQL\database\DB_Homicidios.csv' DELIMITER ';' CSV HEADER;

UPDATE tabla_municipios_departamentos set Region = Upper(Region), Departamento = Upper(Departamento), Municipio = Upper(Municipio);

CREATE TABLE PUBLIC.departamento(
	Codigo_Dane_Departamento integer PRIMARY KEY,
	Nombre_Departamento varchar(100) NOT NULL
);


CREATE TABLE PUBLIC.municipio(
	Codigo_Municipio_Dane integer PRIMARY KEY,
	Nombre_Muncipio varchar(100) NOT NULL,
	Codigo_Dane_Departamento integer NOT NULL,
	FOREIGN KEY (Codigo_Dane_Departamento) 
		REFERENCES departamento(Codigo_Dane_Departamento)
);

CREATE TABLE PUBLIC.tipo_arma(
	ID_tipo_arma serial PRIMARY KEY,
	Nombre_arma varchar(50) NOT NULL
);

CREATE TABLE PUBLIC.genero_victimario(
	ID_genero_victimario serial PRIMARY KEY,
	Nombre_genero varchar(25)
);

CREATE TABLE PUBLIC.grupo_etario(
	ID_grupo_etario serial PRIMARY KEY,
	Nombre_grupo_etario varchar(50) 
);

CREATE TABLE PUBLIC.tipo_homicidio(
	ID_tipo_homicidio serial PRIMARY KEY,
	Nombre_tipo_homicidio varchar(50) 
);

CREATE TABLE PUBLIC.homicidios_colombia(
	ID_caso serial PRIMARY KEY,
	Fecha_homicidio date NOT NULL,
	Numero_Victimas integer NOT NULL,
	ID_tipo_homicidio integer NOT NULL,
	ID_tipo_arma integer NOT NULL,
	ID_genero_victimario integer NOT NULL,
	ID_grupo_etario_victimario integer NOT NULL,
	Codigo_Dane_municipio integer NOT NULL,
	FOREIGN KEY (ID_tipo_homicidio) 
        REFERENCES tipo_homicidio(ID_tipo_homicidio),
	FOREIGN KEY (ID_tipo_arma) 
        REFERENCES tipo_arma(ID_tipo_arma),
	FOREIGN KEY (ID_genero_victimario) 
        REFERENCES genero_victimario(ID_genero_victimario),
	FOREIGN KEY (ID_grupo_etario_victimario) 
        REFERENCES grupo_etario(ID_grupo_etario),
	FOREIGN KEY (Codigo_Dane_municipio) 
        REFERENCES Municipio(Codigo_Municipio_Dane)	
);