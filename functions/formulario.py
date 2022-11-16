import streamlit as st
from data.dataFunctions import conectar, juntarDf
def formInicial():

    nota = 0
    levelUser= ""

    placeholder = st.empty()
    levelUser= ''

    
    with placeholder.container():

        nota = 0
        st.title("FORMULARIO DE AYUDA AL CLIENTE")
        st.write("Responde este pequeño formulario para poder ayudarlo a escojer su automovil ideal")
        preg1 = st.radio("¿Es tu primer auto?", ('.','Si','No'))
        preg2 = st.radio("¿Posee conocimientos tecnicos sobre el auto que desea comprar?", ('.','Si','No'))
        if preg2 == "Si":


            preg3 = st.selectbox("¿En que unidad se mide la presión de los neumaticos de un auto?", ('Kelvin', 'Bares','mmHg'))
            if preg3 == 'Bares':
                nota +=1

            preg4 = st.selectbox("un auto con motor mas grande consume más combustible que uno con motor chico...", ('Verdadero','Falso'))
            if preg4 == 'Verdadero':
                nota +=1

            preg5 = st.selectbox("¿Cuando gasta mas compustible el vehiculo?", ('A altas RPM','A bajas RPM'))
            if preg5 == 'A altas RPM':
                nota +=1

        
        
                
        


       
        # Every form must have a submit button.
        submitted = st.button("Responder")
        
        if submitted:
        
            if preg1 == "Si" and preg2 == "NO" and nota <3:
                levelUser = "Novato"
            elif nota == 3:
                levelUser='Experto'
            
            
            placeholder.empty()
            

            
    return levelUser
            
            
            




