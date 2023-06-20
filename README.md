# Nequi

# Paso 1: Alcance del proyecto y captura de datos

## Identificar y recopilar los datos que usaras para tu proyecto.
    
Dados los criterios sugeridos en los cuales el dataset debe ser publico y debe tener más de 1 millon de datos (filas), se recopilan los datos de la fuente Kaggle: [https://www.kaggle.com/datasets/sanlian/online-retail-dataset](https://www.kaggle.com/datasets/sanlian/online-retail-dataset)
    
[https://archive.ics.uci.edu/dataset/502/online+retail+ii](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
    

## Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis, aplicación de fondo, base de datos de fuentes de verdad, etc.
Tabla de análisis del comportamiento de facturación: Examinar los patrones de compra de los clientes. Podremos identificar segmentos de clientes, determinar su frecuencia de compra, comprender mejor el comportamiento del cliente y optimizar la estrategias de marketing y fidelización.

# Paso 2: Explorar y evaluar los datos, el EDA

## Explorar los datos para identificar problemas de calidad de los datos, como valores perdidos, datos duplicados, problemas de formato etc.
    
Para explorar los datos se siguen los pasos propuestos en el siguiente paso. Los resultados fueron:
    
1. **Lectura de datos:** 
        “Numero de registros del dataset: 1067371”
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
        
5. **Exploración consistencia en datos:** En este caso en particular es importante verificar que los datos numericos esten dentro del rango numero logico, por ejemplo si hablamos de edad no sean negativos. En ese caso “Price” y “Customer ID” no sean negativos; los valores de la columna “Quantity” pueden ser negativos ya que refleja un reembolso de articulos.
    

## Documentar los pasos necesarios para limpiar los datos, indicar que tipo de pasos se sugieren para la limpieza. Tip se puede usar un diagrama, mapa mental o adición en la arquitectura del paso siguiente con el fin de dejar claro este paso.

<p align="center">
  <img src="https://github.com/danilomoreno98/nequi/blob/main/images/Diagramas%20-EDA.drawio.png">
</p>

# Paso 3: Definir el modelo de datos

## Trazar el modelo de datos conceptual y explicar por qué se eligió ese modelo.
    
A continuación se traza el modelo conceptual, la explicación detallada se encuentra en el “**Punto 5: Completar la redacción del proyecto”**
<p align="center">
<img src="https://github.com/danilomoreno98/nequi/blob/main/images/Modelos%20de%20datos%20dimensional.png">
</p>

## Diseñar la arquitectura y los recursos utilizados.

<p align="center">
    <img src="https://github.com/danilomoreno98/nequi/blob/main/images/Arquitectura%20-%20Nequi.png">
    </p>

## Indique claramente los motivos de la elección de las herramientas y tecnologías para el proyecto.

Nota: Se propone que los datos fuentes se encuentran almacenados en una base de datos relacional tipo PostgreSQL dentro de AWS, denotada como **CRM Invoices** y contiene los mismos datos del dataset propuesto.

La solución cuenta con 4 capas, las cuales se describen a continuación:

1. **Capa de ingesta:** En esta etapa suceden todas las ingestas de las diferentes fuentes de información para este caso en particular los datos son ingestados mediante el servicio de Glue de AWS, con la ayuda de Jobs de Glue, posterior se proponen ser almacenados en una primera etapa en una zona de denominada “Raw” dentro de un bucket de S3. Posterior a esto, dicha información nueva es rastreada con ayuda de los Crawler de S3 para ser catalogada en el Glue Catalog. Se propone debido a los siguientes motivos:
    1. Su facil integración con fuentes de datos transaccionales ya que solo basta con configurar el conector mediante JDBC lo que admite una amplia variedad de conectores para diferentes bases de datos transaccionales, como Amazon RDS, Amazon Redshift, Microsoft SQL Server, MySQL, Oracle y otros, facilitando la flexibilidad si se requiere ingestar datos desde otra fuente.
    2. Es escalable, acil de configurar y ajustar la capacidad de procesamiento, lo que permite extraer informacion de grandes bases de datos.
    3. Su facil integración con otros servicios de AWS como S3, lo que te permite aprovechar el ecosistema completo de herramientas y servicios de la nube.
    4. Es un servicio costo-eficiente ya que solo pagamos por el tiempo que dure la extracción de los datos
    
    Tener en cuenta que para esta primer etapa se propone que la información sea ingestada incrementalmente y almacenada en particiones por año/mes/dia dentro de S3 de AWS en la zona “Raw”, esto con el fin de que el catalogo de Glue se active el particionado por el index de tiempo (año/mes/dia) y más adelante en la siguiente capa los datos puedan ser consultados de forma eficiente y rapida, tambien pensando en mantener un buen rendimeinto a largo plazo.
    
2. **Capa de procesamiento y modelado:**  Una vez los datos sean ingestados y almacenados en la zona “Raw” de S3, empiezará el procesamiento y modelado dimensional para la solución analitica. La propuesta sugiere a dbt como herramienta de transformación y modelamiento de los datos, debido a:
    1. Asegura de forma rapida y sencilla con ayuda de SQL que los resultados sean coherentes y predecibles
    2. Incorpora pruebas que permite definir casos de prueba para los modelos de datos durante las diferentes etapas (Silver,Gold). Esto ayuda a verificar la calidad de las transformaciones y a detectar posibles problemas o inconsistencias en los datos.
    3. Se propone utilizar dbt detro de una arquitectura de microservicios lo que permite escalabilidad con el fin de manejar grandes volumenes de datos si es necesario.Ya que la propuesta consta de ejecutar pods dentro de un cluster de EKS con una imagen previamente construida que contenga dbt, mediante el KubernetesPodOperator de Airflow.
    4. Es compatible con control de versiones en las consultas SQL, tambien en este caso la versión estará dada por  una imagen de docker almacenada desde el repositorio de AWS, conocido como ECR (Elastic Container Register).
    
    Cada etapa consta de caracteristicas definidas, en la capa “Raw” se almacenan los datos originales, sin procesar, en nuestro caso los datos provenientes del dataset descrito en el paso 1 y almacenados por la capa de ingesta anteriormente descrita. En la capa “Silver” representa una versión enriquecida, limpia con reglas de negocio, columnas renombradas (si es necesario) y validada de los datos en la que se puede confiar para el análisis posterior. En la ultima capa denominada “Gold” los datos se modelan y enriquecen (agregaciones) para transformar esos datos en conocimiento util para el negocio, datos que finalmente se alojaran en un modelo dimensional en el Datawarehouse, en la solución con el servicio de AWS Redshift.
    
3. **Capa de reporte:** Esta capa finalmente se visualizará la información alojada y modelada de forma adecuada en AWS Redshift mediante una herramienta de BI. En el mercado encontramos multiples herramientas como Power BI, Tableau, Quicksight. En este caso se propone Quicksight.
4. **Capa de orquestación:** Esta capa es transversal ya que sera la encargada de disparar cada uno de los servicios y comunicar las etapas antes mencionadas, como herramienta de orquestación se sugiere Apache Airflow, debido a:
    1. Airflow permite crear flujos de trabajo complejos y definir la secuencia y la dependencia entre las tareas de forma intuitiva y sencilla con Python
    2. Airflow es altamente flexible y extensible con herramientas de diferentes proveedores, lo que permite integrar fácilmente nuevas funcionalidades y adaptarla a diferentes entornos y requisitos. En este caso integrar Glue, S3, dbt(KubernetesPodOperator), Crawlers, Redshift.
    3. Airflow proporciona una interfaz de usuario (UI) intuitiva para monitorear el estado y el progreso de tus flujos de trabajo. También te permite configurar alertas y notificaciones en caso de que ocurran errores o se cumplan ciertas condiciones, lo que permite reaccionar activamente ante cualquier novedad. Y es muy util para ver el historial de logs de cada intento que ha llevado a cabo, con el fin de mantener la trazavilidad de cada ejecución de los flujos o DAGs orquestados.
    4. Distribuye las tareas en paralelo o serie según como sea el caso de uso, lo que mejora el rendimiento y acelera el procesamiento de datos, util en la solución si en dado caso es posible ejecutar 2 o más modelos dbt al tiempo
    5. Permite cambiar el horario de ejecución de forma muy sencilla en caso de cambios en los requisitos o condiciones del entorno.

## Proponga con qué frecuencia deben actualizarse los datos y por qué.
Para el negocio es necesario generar reportes diarios, por lo cual, la ingesta de datos debe hacerse una vez al dia. Para la hora de extracción es necesario considerar que no se impacte en gran medida el rendimiento de la base de datos transaccional utilizada por el CRM, con el fin de evitar caidas significativas y perdidas de datos, de preferencial deberia realizarce en horas donde el publico no está activamente realizando ordenes de compra en la plataforma, se propone en horas de la madrugada. Una vez re realice la extracción es necesario, consecuentemente ejecutar la capa de de "**Capa de procesamiento y modelado**", para actualizar los datos en el Datawarehouse.

# Paso 4: Ejecutar la ETL

## Crear las tuberías de datos y el modelo de datos
## Ejecutar controles de calidad de los datos para asegurar que la tubería funcionó como se esperaba
## Control de calidad en los datos con la integridad en la base de datos relacional (por ejemplo, clave única, tipo de datos, etc.)
## Pruebas de unidad para los “Script” para asegurar que están haciendo lo correcto.
## Comprobaciones de fuente/conteo para asegurar la integridad de los datos.
## Incluir un diccionario de datos
## Criterio de reproducibilidad

# Paso 5: Completar la redacción del proyecto

## ¿Cuál es el objetivo del proyecto?
Generar un reporte de la cantidad y total facturado de los productos entregados y devueltos durante los años 2009 a 2011, habilitando un detalle de fecha diario, desglosado por:
    - Codigo del producto
    - Identificador cliente, pais
    - Codigo de orden
    - Dia de facturación

## ¿Qué preguntas quieres hacer?
    - ¿ Cuantas fueran las unidades vendidas por cada producto ?
    - ¿ Cuales son los productos más vendidos ?
    - ¿ Cual es el pais de origen de los usuarios que más compraron ?
    - ¿ Total de productos se venden en cada mes, año ?
    - Productos que más se venden en cada mes del año

## ¿Por qué eligió el modelo que eligió?
Debido al objetivo y preguntas planteadas para el negocio que nos gustaria resolver, se identifica que la información que da contexto o describe las transacciones es: información del usuario, información del producto, información de la fecha de la transacción e información del cliente. Por lo cual la información que representa el proceso de negocio se basa en cada transacción de la facturación con sus cantidades cuantitativas, lo que se traduciria en una tabla de hechos. De esta forma llegamos a un claro acercamiento de un modelo dimensional tipo estrella.
    
## Incluya una descripción de cómo abordaría el problema de manera diferente en los siguientes escenarios:
- Si los datos se incrementaran en 100x<br />
    - Para tener un rendimiento favorable, se piensa implementar una estrategia de partición de los datos desde la etapa "Raw", como se mencióno en las descripción de las capas de la arquitectura en el **Punto 3, sección: Diseñar la arquitectura y los recursos utilizados**. Con una partición planteada en el catalogo de Glue podemos mantener un buen rendimiento en escenarios donde el volumen de datos diarios suba. Tambien de cara al Datawarehuse se debe pensar en una sortkey por fecha para mejorar las consultas y evitar consultas que tarden demasiado tiempo.
- Si las tuberías se ejecutaran diariamente en una ventana de tiempo especifica.<br />
    - Gracias a Airflow como orquestador de la solución un cambio en el horario de ejecucion de los pipeline, se puede hacer de forma muy facil, solo basta con configurar la nueva expresión crontab en la ventana especifica de tiempo.
- Si la base de datos necesitara ser accedido por más de 100 usuarios funcionales.<br />
    - Si nuestro Datawarehouse es accedido por varios usuarios funcionales, tenemos 2 opciones:
        1. Implementar un proxy para optimizar y evitar que sufra nuestro Datawarehouse, la ventaja es que es una solución NO CODE, en el siguiente link se puede profundizar sobre esta solución: https://aws.amazon.com/es/blogs/apn/improving-application-performance-with-no-code-changes-using-heimdalls-database-proxy-for-amazon-redshift/
        2. Implemetar una base de datos en memoria para mejorar el rendimiento y que los usuarios funcionales no tengan problemas en consultar la información común consultada y obtener carga de datos en un tiempo optimo. Esto tambien es posible con herramientas nativas de AWS como Spice del visualizador Quicksight.
- Si se requiere hacer analítica en tiempo real, ¿cuales componentes cambiaria a su arquitectura propuesta? <br />
    Para ingestar datos en tiempo real, tocaria cambiar el job de Glue Clasico por un **AWS Kinesis Data Stream**, combinado por un **job de Glue en Streaming** para habilitar la capacidad de ingestar datos en real time.