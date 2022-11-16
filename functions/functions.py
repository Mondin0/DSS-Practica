import streamlit as st
from functions.formulario import formInicial


def matrizNovato(dataframe,a,b,c):
    dataframe['Puntuacion'] = (dataframe['C'] * (1 - a) + 10) + \
                             (dataframe['P'] * b + 10) + (dataframe['S'] * c)
    return dataframe



def defineInterfaz(levelUser,dataframe):
    if levelUser == 'Novato':
        st.write("Interfaz Novato")
        interfazNovato(dataframe)
        
    elif levelUser == "Experto":
        st.write("Interfaz Experto")
        interfazExperto(dataframe)
    
        
        

def interfazPrincipal(dataframe):
        principal = st.empty()
        with principal.container():
            st.title("AUTOS ISFDyT124")
            st.write('Especifique la marca y el precio para ver los automoviles disponibles que cumplan su requisito')
            marcaP = st.multiselect('Marca del vehículo', sorted(dataframe['Marca'].unique().tolist()))
            
            if marcaP == []:
                st.warning("Seleccione una Marca")
            precio_max = st.number_input('Precio en miles de pesos, el máximo es de $10.000', min_value=0,key="precio_principal",step=1000)
            if precio_max == 0:
                st.warning("Indique el precio maximo que desea")
            elif precio_max > 10000:
                st.error("El precio maximo no debe superar los 10000$")
            filtrado = dataframe[(dataframe['Marca'].isin(marcaP)) & (dataframe['Precio'] < precio_max)]
            num_resultados = len(filtrado)
            with st.expander(f'Tenemos {num_resultados} automoviles que cumplen con sus requisitos '):
                st._arrow_table(
                filtrado.loc[:, ['Marca', 'Modelo', 'Version', 'Precio', ]].sort_values(by='Precio',
                                                                                                    ascending=True),
            )


        #FORMULARIO DE AYUDA AL CLIENTE
            st.info("Si necesitas ayuda precione la opcion de AYUDA PROFESIONAL")
        
        formulario = st.empty()
        with formulario.expander("AYUDA PROFESIONAL"):
            placeholder = st.empty()
            levelUser= ''
    
            with placeholder.container():

                nota = 0
                st.title("FORMULARIO DE AYUDA AL CLIENTE")
                st.write("Responde este pequeño formulario para poder ayudarlo a escojer su automovil ideal")
                preg1 = st.radio("¿Es tu primer auto?", ('.','Si','No'))
                st.write(preg1)
                preg2 = st.radio("¿Posee conocimientos tecnicos sobre el auto que desea comprar?", ('.','Si','No'))
                
                if preg2 == "Si":
                    st.write("Seleccione la opcion que le parezca correta y continue")
                    preg3 = st.selectbox("¿En que unidad se mide la presión de los neumaticos de un auto?", ('Kelvin', 'Bares','mmHg'))
                    if preg3 == 'Bares':
                        nota +=1

                    preg4 = st.selectbox("un auto con motor mas grande consume más combustible que uno con motor chico...", ('Verdadero','Falso'))
                    if preg4 == 'Verdadero':
                        nota +=1

                    preg5 = st.selectbox("¿Cuando gasta mas compustible el vehiculo?", ('A altas RPM','A bajas RPM'))
                    if preg5 == 'A altas RPM':
                        nota +=1

                    
                
                st.write(nota)
                # Every form must have a submit button.
                submitted = st.button("Responder")
                
                if submitted:
                    
                    if preg1 == "Si" and preg2 == "NO" or nota < 2:
                        levelUser = "Novato"
                    elif nota == 3:
                        levelUser='Experto'
                    principal.empty()
                    placeholder.empty()
                    formulario.empty()
                    
                    
                    
                    
                                
        return levelUser
            
        
               
                
                
                
        
        
        



def interfazNovato(dataframe):
    st.success("** Interfaz Novato **")
    
    st.header('Segun lo respondido anteriormente hemos escojido las siguientes opciones:')
    st.info('Selecciona lo que consideres mas importante para tu futuro vehículo')
    
    select_consumo = st.slider('Bajo Consumo',1,5,)
    if select_consumo == 1 or select_consumo == 2:
        st.success("Bajo Consumo")
    elif select_consumo == 3:
        st.warning("Consumo moderado")
    elif select_consumo > 3:
        st.error("Alto Consumo")
    
    select_potencia = st.slider('Potencia', 1,5)
    if select_potencia == 1 or select_potencia == 2:
        st.error("Baja Potencia")
    elif select_potencia == 3:
        st.warning("Potencia Moderada")
    elif select_potencia > 3:
        st.success("Alta Potencia")
    
    
    select_seguridad = st.slider('Seguridad', 1,5)
    if select_seguridad == 1 or select_potencia == 2:
        st.warning("Seguridad Baja")
    elif select_seguridad == 3:
        st.info("Seguridad Aceptable")
    elif select_seguridad > 3:
        st.success("Seguridad Alta")

    marca = st.multiselect('Marca del vehículo', sorted(dataframe['Marca'].unique().tolist()),key="novato")
    precio_max = st.number_input('Precio en miles de pesos, el máximo es de $10.000', min_value=0, max_value=10000,key="precio_novato",step=1000)
    st.info(f"Precio Maximo: {precio_max}000$")
    filtrado = dataframe[(dataframe['Marca'].isin(marca)) & (dataframe['Precio'] < precio_max)]
    ponderacion = matrizNovato(filtrado, select_consumo,select_potencia,select_seguridad)

    st._arrow_table(
            ponderacion.loc[:, ['Marca', 'Modelo', 'Version', 'Precio', 'Puntuacion']].sort_values(by='Puntuacion',
                                                                                                ascending=False),
        )

     
        



            


def interfazExperto(dataframe):
    st.success("** Interfaz Experto **")
    st.header('Segun lo respondido anteriormente hemos escojido las siguientes opciones:')
    st.info('Selecciona lo que consideres mas importante para tu futuro vehículo')
    
    
    
    select_consumo = st.radio('Bajo Consumo', [1, 2, 3, 4, 5],horizontal=True)
    select_potencia = st.radio('Potencia', [1, 2, 3, 4, 5],horizontal=True)
    select_seguridad = st.radio('Seguridad', [1, 2, 3, 4, 5],horizontal=True)
    marca = st.multiselect('Marca del vehículo', sorted(dataframe['Marca'].unique().tolist()),default=dataframe["Marca"][0],key="experto")

   
    

    tipo = st.multiselect("Tipo de vehiculo",dataframe["TipoVehiculo"].unique().tolist())


    transmision = st.multiselect("Transmision del vehiculo",dataframe["Transmisión"].unique().tolist())

    precio_max = st.number_input('Precio en miles de pesos, el máximo es de $10.000', min_value=0, max_value=10000,key="precio_novato",step=1000)
    st.info(f"Precio Maximo: {precio_max}000$")

    filtrado = dataframe[(dataframe['Marca'].isin(marca)) & (dataframe['Precio'] < precio_max) & (dataframe["TipoVehiculo"].isin(tipo))]
    ponderacion = matrizNovato(filtrado, select_consumo,select_potencia,select_seguridad)

    st._arrow_table(
            ponderacion.loc[:, ['Marca', 'Modelo', 'Version','TipoVehiculo', 'Precio', 'Puntuacion']].sort_values(by='Puntuacion',
                                                                                                ascending=False),
        )



def documentacion():

    st.write("[Manual de usuario](https://github.com/Mondin0/DSS-Practica.git)")


    
  
   
 


