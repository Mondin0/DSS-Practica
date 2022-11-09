import streamlit as st
from data.dataFunctions import conectar, juntarDf
def formInicial():

    nota = 0
    levelUser= ""

    placeholder = st.empty()
    levelUser= ''

    with placeholder.form("my_form"):
        

        st.write("Responde este pequeño formulario")

        preg1 = st.radio("¿Que es el torque?", ('La fuerza del motor','La tracción','La velocidad de arranque'))
        preg2 = st.selectbox("¿Que significa HP?", ('Caballo de fuerza','Hewlet Packard','Ninguna de las anteriores'))
        preg3 = st.selectbox("¿En que unidad se mide la presión de los neumaticos de un auto?", ('Kelvin', 'Bares','mmHg'))
        preg4 = st.selectbox("un auto con motor mas grande consume más combustible que uno con motor chico...", ('Verdadero','Falso'))
        preg5 = st.selectbox("¿Cuando gasta mas compustible el vehiculo?", ('A altas RPM','A bajas RPM'))
        
        nota = 0

        if preg1 == 'La fuerza del motor':
            nota +=1
        if preg2 == 'Caballo de fuerza':
            nota +=1
        if preg3 == 'Bares':
            nota +=1
        if preg4 == 'Verdadero':
            nota +=1
        if preg5 == 'A altas RPM':
            nota +=1
       
        # Every form must have a submit button.
        submitted = st.form_submit_button("Responder")
        
        if submitted:
        
            if nota <=3 and nota > 0:
                levelUser='Novato'
            elif nota >= 4 and nota > 0:
                levelUser='Experto'
            
            st.write(levelUser)
            placeholder.empty()
            
    return levelUser
            
            
            




