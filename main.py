import streamlit as st
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import defineInterfaz,interfazNovato,interfazExperto
from functions.formulario import formInicial

con = conectar()

dataframe = juntarDf(con)


levelUser = formInicial()

defineInterfaz(levelUser,dataframe)


"comentario"



desconectar(con)


