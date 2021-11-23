def homicidiosPorDepartamento():
    return """SELECT d.Nombre_Departamento as departamento, COUNT(hc.ID_caso) as homicidios
            FROM homicidios_colombia hc, departamento d, municipio mc
            WHERE hc.Codigo_Dane_municipio = mc.Codigo_Municipio_Dane AND mc.Codigo_Dane_Departamento = d.Codigo_Dane_Departamento
            GROUP BY (d.Nombre_Departamento)"""

def armasHomicidios():
    return """SELECT ar.Nombre_arma as Arma, COUNT(hc.ID_caso) as Homicidios
            FROM  homicidios_colombia hc, tipo_arma ar
            WHERE hc.ID_tipo_arma = ar.ID_tipo_arma
            GROUP BY (ar.Nombre_arma)"""

def generoVictimarios():
    return """SELECT gen.Nombre_genero as genero, COUNT(hc.ID_caso) as homicidios
            FROM homicidios_colombia hc, genero_victimario gen
            WHERE hc.ID_genero_victimario = gen.ID_genero_victimario
            GROUP BY (gen.Nombre_genero)"""

def homicidiosPorAño():
    return """SELECT EXTRACT(year From hc.Fecha_homicidio) AS año, COUNT(ID_caso) AS homicidios
            From homicidios_colombia hc
            Group BY (EXTRACT(year From hc.Fecha_homicidio))
            ORDER BY (año)"""
            
def homicidios_municipios():
    return """select municipio.nombre_muncipio as municipio, sum(Numero_victimas) as homicidios
            from homicidios_colombia join municipio on (homicidios_colombia.Codigo_Dane_municipio = municipio.Codigo_Municipio_Dane)
            group by municipio.nombre_muncipio
            order by sum(Numero_victimas) desc
           """
           
def edad_victimarios():
    return """SELECT Nombre_Grupo_Etario AS grupo_etario, count(ID_caso) as homicidios
            FROM Grupo_Etario ge, homicidios_colombia hc
            WHERE ge.ID_grupo_etario = hc.ID_grupo_etario_victimario
            GROUP BY Nombre_Grupo_Etario
              """


            
