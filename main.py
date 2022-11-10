import streamlit as st
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import defineInterfaz,interfazNovato,interfazExperto
from functions.formulario import formInicial

con = conectar()
dataframe = juntarDf(con)

#levelUser= st.selectbox("nivel de usuario", ["Novato", "Experto"])
levelUser= formInicial()
#st.write(levelUser)
defineInterfaz(levelUser,dataframe)






desconectar(con)


