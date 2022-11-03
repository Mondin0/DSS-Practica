import streamlit as st
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import interfazNovato
from functions.formulario import formInicial

con = conectar()
dataframe = juntarDf(con)

formInicial()


interfazNovato(dataframe)

desconectar(con)


