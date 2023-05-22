# PROYECTO POS STORE 
Sistema de POS para el curso de django avanzado II
## Pasos para la instalación del software

Este proyecto inicio desde el año 2019 para los siguientes cursos de mi canal de [Youtube](https://www.youtube.com/c/AlgoriSoft "Youtube"):

- [Curso de Python con Django de 0 a Máster | Español](https://youtube.com/playlist?list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7 "Curso de Python con Django de 0 a Máster | Español")
- [Curso de Deploy de un Proyecto Django en un VPS Ubuntu | Español](https://youtube.com/playlist?list=PLxm9hnvxnn-hFNSoNrWM0LalFnSv5oMas "Curso de Deploy de un Proyecto Django en un VPS Ubuntu | Español")
- [Curso de Python con Django Avanzado | Español](https://www.youtube.com/playlist?list=PLxm9hnvxnn-gvB0h0sEWjAf74ge4tkTOO "Curso de Python con Django Avanzado | Español")

# Instaladores

| Nombre                   | Instalador                                                                                                                                                                                                                     |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| `Compilador`             | [Python3](https://www.python.org/downloads/release/python-396/ "Python3")                                                                                                                                                      |
| `IDE de programación`    | [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code"), [Sublime Text](https://www.sublimetext.com/ "Sublime Text"), [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows "Pycharm") |
| `Motor de base de datos` | [Sqlite Studio](https://github.com/pawelsalawa/sqlitestudio/releases "Sqlite Studio"), [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL"), [MySQL](https://www.apachefriends.org/es/index.html "MySQL") |

# Pasos de instalación

##### 1) Clonar el repositorio del proyecto en un directorio de tu computador o servidor

##### 2) Crear un entorno virtual para la instalación de las librerías del proyecto

Para windows:

```bash
python3 -m venv venv 
```

Para linux:

```bash
virtualenv venv -ppython3 
```

##### 3) Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint") para imprensión de archivos pdf

Si estas usando Windows debe descargar el complemento de [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases "GTK3 installer"). En algunas ocaciones se debe colocar en las variables de entorno como primera para que funcione y se debe reiniciar el computador.

Si estas usando Linux debes instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador.

##### 4) Activar el entorno virtual de nuestro proyecto

Para windows:

```bash
cd venv\Scripts\activate.bat 
```

Para Linux:

```bash
source venv/bin/active
```

##### 5) Instalar todas las librerias del proyecto que se encuentran en la carpeta deploy

```bash
pip install -r deploy/txt/requirements.txt
```

##### 6) Crear la tablas de la base de datos a partir de las migraciones de django

```bash
python manage.py makemigrations
python manage.py migrate
```

##### 7) Insertar datos iniciales en las entidades de los módulos de seguridad y usuario del sistema

```bash
python manage.py shell --command='from core.init import *'
```

##### 8) Insertar datos iniciales de categorías, productos, clientes y ventas aleatorias (Paso opcional)

```bash
python manage.py shell --command='from core.utils import *'
```

##### 9) Iniciar el servidor del proyecto

```bash
python manage.py runserver 
```

Si deseas verlo en toda tu red puedes ejecutarlo asi:

```bash
python manage.py runserver 0:8000 o python manage.py runserver 0.0.0.0:8000
```

##### 10) Iniciar sesión en el sistema (Puede cambiar la clave y usuario que se crea en el archivo core/init.py del paso 7)

```bash
username: admin
password: hacker94
```

------------

#  Gracias por tomar mi curso ✅🙏
#### Esto me sirve mucho para seguir produciendo mi contenido 🤗​
### ¡Apóyame! para seguir haciéndolo siempre 😊👏
Paso la mayor parte de mi tiempo creando contenido y ayudando a futuros programadores sobre el desarrollo web con tecnología open source.

🤗💪¡Muchas Gracias!💪🤗

**Puedes apoyarme de la siguiente manera.**

**Suscribiéndote**
https://www.youtube.com/c/AlgoriSoft?sub_confirmation=1

**Siguiendo**
https://www.facebook.com/algorisoft

**Donando por PayPal**
williamjair94@hotmail.com

***AlgoriSoft te desea lo mejor en tu aprendizaje y crecimiento profesional como programador 🤓.***


