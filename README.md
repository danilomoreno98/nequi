# Nequi

# Paso 1: Alcance del proyecto y captura de datos

- Identificar y recopilar los datos que usaras para tu proyecto.
    
    Dados los criterios sugeridos en los cuales el dataset debe ser publico y debe tener más de 1 millon de datos (filas), se recopilan los datos de la fuente Kaggle: [https://www.kaggle.com/datasets/sanlian/online-retail-dataset](https://www.kaggle.com/datasets/sanlian/online-retail-dataset)
    
    [https://archive.ics.uci.edu/dataset/502/online+retail+ii](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
    

- Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis, aplicación de fondo, base de datos de fuentes de verdad, etc.)
    
    Tabla de análisis del comportamiento del cliente: Examinar los patrones de compra de los clientes. Podremos identificar segmentos de clientes, determinar su frecuencia de compra, comprender mejor el comportamiento del cliente y optimizar la estrategias de marketing y fidelización.
    

# Paso 2: Explorar y evaluar los datos, el EDA

- Explorar los datos para identificar problemas de calidad de los datos, como valores perdidos, datos duplicados, problemas de formato etc.
    
    Para explorar los datos se siguen los pasos propuestos en el siguiente paso. Los resultados fueron:
    
    1. **Lectura de datos:** “Numero de registros del dataset: 1067371”
    2. **Exploración cantidad de variables y tipo:** Se deja como observación que la columna denominada “Customer ID” debe ser tratada como tipo int
        
        **** Exploración cantidad de variables y tipo *****
        Columna: Invoice -> Tipo: object
        Columna: StockCode -> Tipo: object
        Columna: Description -> Tipo: object
        Columna: Quantity -> Tipo: int64
        Columna: InvoiceDate -> Tipo: datetime64[ns]
        Columna: Price -> Tipo: float64
        Columna: Customer ID -> Tipo: float64
        Columna: Country -> Tipo: object
        
    3. **Exploración datos nulos:** Se deja como observación que la columna descripción null cuenta con datos en blanco, sin embargo, para el negocio no es mandatorio que tenga información. Sin embargo, para la columna denominada “Customer ID” es mandatorio que no tenga valores null como regla de negocio, por tanto, toca aplicar reglas de calidad para esta novedad.
        
        **** Exploración datos nulos *****
        
        Invoice             0
        StockCode           0
        Description      4382
        Quantity            0
        InvoiceDate         0
        Price               0
        Customer ID    243007
        Country             0
        dtype: int64
        
    4. **Exploración datos duplicados:** Dado que el dataset consta de registros de transacciones, se van  a encontrar registros duplicados, sin embargo, se analizará el numero unico de transacciones( ya que una factura se repite n numero de productos) y lo mismo sucede con el usuario, a continuacion los resultados:
        
        **** Exploración valores unicos, columna 'Invoice': 53628 *****
        
        **** Exploración valores unicos, columna 'Customer ID': 5942 *****
        
    
    1. **Exploración consistencia en datos:** En este caso en particualar es importante verificar que los datos numericos esten dentro del rango numero logico, por ejemplo si hablamos de edad no sean negativos. En ese caso “Price” y “Customer ID” no sean negativos; los valores de la columna “Quantity” pueden ser negativos ya que refleja un reembolso de articulos.
    

- Documentar los pasos necesarios para limpiar los datos, indicar que tipo de pasos se sugieren para la limpieza. Tip se puede usar un diagrama, mapa mental o adición en la arquitectura del paso siguiente con el fin de dejar claro este paso.

https://github.com/danilomoreno98/nequi/blob/main/images/Diagramas%20-EDA.drawio.png

# Paso 3: Definir el modelo de datos

- Trazar el modelo de datos conceptual y explicar por qué se eligió ese modelo.
- Diseñar la arquitectura y los recursos utilizados.
- Indique claramente los motivos de la elección de las herramientas y tecnologías para el proyecto.
- Proponga con qué frecuencia deben actualizarse los datos y por qué.

# Paso 4: Ejecutar la ETL

- Crear las tuberías de datos y el modelo de datos
- Ejecutar controles de calidad de los datos para asegurar que la tubería funcionó como se
esperaba
- Control de calidad en los datos con la integridad en la base de datos relacional (por ejemplo,
clave única, tipo de datos, etc.)
- Pruebas de unidad para los “Script” para asegurar que están haciendo lo correcto.
- Comprobaciones de fuente/conteo para asegurar la integridad de los datos.
- Incluir un diccionario de datos
- Criterio de reproducibilidad

# Paso 5: Completar la redacción del proyecto

- ¿Cuál es el objetivo del proyecto?
- ¿Qué preguntas quieres hacer?
- ¿Por qué eligió el modelo que eligió?
- Incluya una descripción de cómo abordaría el problema de manera diferente en los siguientes
escenarios:
    - Si los datos se incrementaran en 100x
    - Si las tuberías se ejecutaran diariamente en una ventana de tiempo especifica.
    - Si la base de datos necesitara ser accedido por más de 100 usuarios funcionales.
    - Si se requiere hacer analítica en tiempo real, ¿cuales componentes cambiaria a su
    arquitectura propuesta?