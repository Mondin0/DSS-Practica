import streamlit as st
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import defineInterfaz,interfazNovato,interfazExperto,interfazPrincipal,documentacion
from functions.formulario import formInicial

con = conectar()

dataframe = juntarDf(con)



levelUser = interfazPrincipal(dataframe)
# interfaz = defineInterfaz(levelUser, dataframe)

documentacion()






desconectar(con)


