import streamlit as st
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import defineInterfaz
from functions.formulario import formInicial

con = conectar()
dataframe = juntarDf(con)


levelUser = formInicial()
defineInterfaz(levelUser,dataframe)

desconectar(con)


