import streamlit as st


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
        
        



def interfazNovato(dataframe):
    
    st.title('¿Querés comprarte un auto? Nosotros te ayudamos')
    with st.expander('Este es un listado de los autos que te pueden aparecer como opcion final'):
        st.dataframe(dataframe)
    st.header('Selecciona lo que consideres mas importante para tu futuro vehículo')
    st.subheader('Elegir prioridad en orden ascendente')
    consumo = {"Bajo":1,"Medio":2,"Alto":3}
    select_consumo = st.selectbox('Bajo Consumo', [1,2,3,4,5],1)
    select_potencia = st.selectbox('Potencia', [1, 2, 3, 4, 5])
    select_seguridad = st.selectbox('Seguridad', [1, 2, 3, 4, 5])
    marca = st.multiselect('Marca del vehículo', sorted(dataframe['Marca'].unique().tolist()))
    precio_max = st.number_input('Precio en miles de pesos, el máximo es de $10.000', min_value=0, max_value=10000)
    filtrado = dataframe[(dataframe['Marca'].isin(marca)) & (dataframe['Precio'] < precio_max)]
    ponderacion = matrizNovato(filtrado, select_consumo,select_potencia,select_seguridad)

    with st.expander('Los resultados son...'):
        st._arrow_table(
            ponderacion.loc[:, ['Marca', 'Modelo', 'Version', 'Precio', 'Puntuacion']].sort_values(by='Puntuacion',
                                                                                                ascending=False),
        )
        



            


def interfazExperto(dataframe):
    st.title("El auto que busques lo encuentras aqui!!")
    
    st.header('Selecciona lo que consideres mas importante para tu futuro vehículo')
    
    st.subheader('Elegir prioridad en orden ascendente')
    
    select_consumo = st.radio('Bajo Consumo', [1, 2, 3, 4, 5],horizontal=True)
    select_potencia = st.radio('Potencia', [1, 2, 3, 4, 5],horizontal=True)
    select_seguridad = st.radio('Seguridad', [1, 2, 3, 4, 5],horizontal=True)
    marca = st.multiselect('Marca del vehículo', sorted(dataframe['Marca'].unique().tolist()),default=dataframe["Marca"][0])

    # with st.multiselect("Modelo",dataframe["Modelo"]) as modelo:
    #     if modelo == None:
    #         st.error("Seleccione un modelo")
    
    

    tipo = st.multiselect("Tipo de vehiculo",dataframe["TipoVehiculo"].unique().tolist())


    transmision = st.radio("Transmision del vehiculo",dataframe["Transmisión"].unique().tolist())


    
  
   
 


