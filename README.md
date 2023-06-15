# Nequi

# Paso 1: Alcance del proyecto y captura de datos

- Identificar y recopilar los datos que usaras para tu proyecto.
    
    Dados los criterios sugeridos en los cuales el dataset debe ser publico y debe tener más de 1 millon de datos (filas), se recopilan los datos de la fuente Kaggle: [https://www.kaggle.com/datasets/sanlian/online-retail-dataset](https://www.kaggle.com/datasets/sanlian/online-retail-dataset)
    
    [https://archive.ics.uci.edu/dataset/502/online+retail+ii](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
    

- Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis, aplicación de fondo, base de datos de fuentes de verdad, etc.)
    
    Tabla de análisis del comportamiento del cliente: Examinar los patrones de compra de los clientes. Podremos identificar segmentos de clientes, determinar su frecuencia de compra, comprender mejor el comportamiento del cliente y optimizar la estrategias de marketing y fidelización.
    

# Paso 2: Explorar y evaluar los datos, el EDA

- Explorar los datos para identificar problemas de calidad de los datos, como valores perdidos, datos duplicados, problemas de formato etc.

- Documentar los pasos necesarios para limpiar los datos, indicar que tipo de pasos se sugieren para la limpieza. Tip se puede usar un diagrama, mapa mental o adición en la arquitectura del paso siguiente con el fin de dejar claro este paso.

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

# Paso 5: Ejecutar la ETL

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
