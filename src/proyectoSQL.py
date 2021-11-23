def homicidiosPorDepartamento():
    return """SELECT d.Nombre_Departamento as departamento, COUNT(hc.ID_caso) as homicidios
            FROM homicidios_colombia hc, departamento d, municipio mc
            WHERE hc.Codigo_Dane_municipio = mc.Codigo_Municipio_Dane AND mc.Codigo_Dane_Departamento = d.Codigo_Dane_Departamento
            GROUP BY (d.Nombre_Departamento)"""
#Esta sentencia SQL muestra los homicidios separados por departamentos, mostrará dos columnas el nombre del departamento 
#y un número de homicidios, posteriormente esta organizado por nombre del departamento. Esta dentro de una función que posteriormente se llamará en proyecto.py

def armasHomicidios():
    return """SELECT ar.Nombre_arma as Arma, COUNT(hc.ID_caso) as Homicidios
            FROM  homicidios_colombia hc, tipo_arma ar
            WHERE hc.ID_tipo_arma = ar.ID_tipo_arma
            GROUP BY (ar.Nombre_arma)
            ORDER BY (COUNT(hc.ID_caso)) DESC"""

## Esta sentencia SQL nos indica el numero de veces que X arma se uso en un homicidio, mostrará dos columnas una con el nombre del arma 
## y la otra con el número de homicidios realizads con ese tipo de arma. Esta dentro de una función que posteriormente se llamará en proyecto.py

def generoVictimarios():
    return """SELECT gen.Nombre_genero as genero, COUNT(hc.ID_caso) as homicidios
            FROM homicidios_colombia hc, genero_victimario gen
            WHERE hc.ID_genero_victimario = gen.ID_genero_victimario
            GROUP BY (gen.Nombre_genero)"""

## Esta sentencia SQL nos indica cuantos victimarios de X género en los homicidios que se tienen registros en la base de datos. Mostrará dos columnas que són 
## el nombre del género y cuantos homicidios cometio ese X genero. Esta dentro de una función que posteriormente se llamará en proyecto.py

def homicidiosPorAño():
    return """SELECT EXTRACT(year From hc.Fecha_homicidio) AS año, COUNT(ID_caso) AS homicidios
            From homicidios_colombia hc
            Group BY (EXTRACT(year From hc.Fecha_homicidio))
            ORDER BY (año)"""

## Esta sentencia SQL nos muestra los homicidios cometidos por año, mostrará dos columnas una será el año y la otra el número de homicidios.
## esta información será ordenada por el año . Esta dentro de una función que posteriormente se llamará en proyecto.py
            
def homicidios_municipios():
    return """select municipio.nombre_muncipio as municipio, sum(Numero_victimas) as homicidios
            from homicidios_colombia join municipio on (homicidios_colombia.Codigo_Dane_municipio = municipio.Codigo_Municipio_Dane)
            group by municipio.nombre_muncipio
            order by sum(Numero_victimas) desc
           """
## Esta sentencia SQL muestra los homicidios por municipios, mostrará dos columnas el nombre del municipio y el número de victimas que ocurrieron.
## Esta información será ordenada de forma descendiente por el número de victimas. Esta dentro de una función que posteriormente se llamará en proyecto.py
           
def edad_victimarios():
    return """SELECT Nombre_Grupo_Etario AS grupo_etario, count(ID_caso) as homicidios
            FROM Grupo_Etario ge, homicidios_colombia hc
            WHERE ge.ID_grupo_etario = hc.ID_grupo_etario_victimario
            GROUP BY Nombre_Grupo_Etario
              """
## Esta sentencia SQL muestra el grupo etario de los victimarios, mostrará dos columnas una será el nombre del grupo etario y la otra será el numero de homicidios
## Esta información sera ordenada por el nombre del grupo etario. Esta dentro de una función que posteriormente se llamará en proyecto.py

            
