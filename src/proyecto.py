import psycopg2
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from Connection import Connection
import proyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

con = Connection()
con.openConnection()
conexion = con.cursor()

query = pd.read_sql_query(sql.homicidiosPorDepartamento(), con.connection)
query2 = pd.read_sql_query(sql.armasHomicidios(), con.connection)
query3 = pd.read_sql_query(sql.generoVictimarios(), con.connection)
query4 = pd.read_sql_query(sql.homicidiosPorAño(), con.connection)
query5 = pd.read_sql_query(sql.homicidios_municipios(), con.connection)
query6 = pd.read_sql_query(sql.edad_victimarios(), con.connection)

con.closeConnection()

datosHomicidiosporDepartamento = pd.DataFrame(query, columns=["departamento", "homicidios"])
datosHomicidiosArmas = pd.DataFrame(query2, columns=["arma", "homicidios"])
datosGeneroVictimarios = pd.DataFrame(query3, columns=["genero", "homicidios"])
datosHomicidiosporAño = pd.DataFrame(query4, columns=["año", "homicidios"])
datosHomicidiosporMunicipio = pd.DataFrame(query5, columns=["municipio", "homicidios"])
datosEdadVictimarios = pd.DataFrame(query6, columns=["grupo_etario", "homicidios"])


hDepartamentos = px.bar(datosHomicidiosporDepartamento.head(32), x="departamento", y="homicidios")
hMunicipio = px.bar(datosHomicidiosporMunicipio.head(20), x="municipio", y="homicidios")
harma = px.bar(datosHomicidiosArmas.head(42), x="arma", y="homicidios")
hgenero = px.pie(datosGeneroVictimarios.head(5), names="genero", values="homicidios")
hedad = px.pie(datosEdadVictimarios.head(5), names="grupo_etario", values="homicidios")
haño = px.line(datosHomicidiosporAño.head(20), x="año", y="homicidios")

app.layout = html.Div(children=[
    html.H1(children='Analisis Homicidios Colombia'),
    html.H2(children='Homicidios por departamento'),
    dcc.Graph(
        id='Homicidios por departamento',
        figure=hDepartamentos
    ),
    html.H2(children='Homicidios por municipio'),
    dcc.Graph(
        id='Homicidios por municipio',
        figure=hMunicipio
    ),  
    html.H2(children='Armas utilizadas en homicidios'),
    dcc.Graph(
        id='Armas utilizadas en homicidios',
        figure=harma
    ),
    html.H2(children='Grupo etario Victimarios'),
    dcc.Graph(
        id='Grupo etario Victimarios',
        figure=hedad
    ),
    html.H2(children='Genero Victimarios'),
    dcc.Graph(
        id='Genero Victimarios',
        figure=hgenero
    ),
    html.H2(children='Homicidios por año'),
    dcc.Graph(
        id='Homicidios por año',
        figure=haño
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)