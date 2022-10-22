# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME

# Actividad

1. Analiza el funcionamiento del script
    
    1.1 ¿Cuál es su entrada?
        Un URL con informacion de peliculas. 
    
    1.2 ¿Qué procesamiento esta haciendo?
        El script lee el url por medio de la libreria BeautifulSoup que permite analizar documentos HTML. Procesa los datos y añade la informacion en columnas correspondientes, convirtiendo la informacion en registros en filas.
    
    1.3 ¿Cuál es su salida?
        Regresa un CSV con la informacion de las peliculas de la pagina web con un formato de tabla en los que los registros estan en filas, en cada columan estan sus atributos. Se veria en columnas y filas si el CSV se importa a excel o numbers, de lo contrario veremos los datos separados por comas. 


2. Una vez identificado el funcionamiento, refactoriza el script en diferentes metodos o clases de tal manera que sea mas facil de leer y de entender.

    Correr el movie_main.py

3. La refactorizacion debe seguir los principios de SOLID vistos en clase.

# IDENTIFICACIÓN DE PRINCIPIOS SOLID

1. Single Responsability Principle
    El primer principio SOLID identificado es el de "The single responsability principle". Este lo encontramos en el modulo
    de exportar porque es un modulo exclusivo para exportar la informacion y dentro de el mismo se encuentran las variaciones por formato. Sin embargo, el modulo se encarga unica y exclusivamente de exportar la informacion por lo que podemos 
    confirmar que se esta haciendo uso del principio. El modulo puede crecer agregando otro tipo de archivos para exportar la informacion 

    Archivo: movie_export.py

2. The Open Close Principle
    El segundo principio SOLID identificado es el de "The Open Close Principle". Este lo encontramos en el modulo de exportar y en el modulo de recibir informacion de una pagina web (movie_getinfo)
    
     ya que este al no estar encapsulando los formatos de exportar en una sola clase permite que se puedan tener otras clases que esten definidas para otros formatos, estando abierot a la extension, pero se sigue manteniendo la funcionalidad de generar reportes sin modificacion alguna. De igual manera sucede con la obtencion de la informacion si se requiere obtener la info desde otro formato se podriahacer extendiendo sin modificacion a lo que ya existe
    
    Archivo exportar: movie_export.py
    Archivo obtener info: movie_getinfo.py

3. The Interface segregation principle (ISP)
    El tercer principio SOLID identificado es el de "The Interface segregation principle (ISP)" este principio lo vemos aplicado en la primera pantalla donde el usuario solo esta siendo presentado la parte de ingresar el url, la fuente de donde quiere obtener la data. Como a el no le interesa el resto de los metodos si no que solo quiere dar la funete de informacion este es el unico metodo con el que interactua. 

    Archivo: movie_main.py