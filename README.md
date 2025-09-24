# PRUEBA-TÉCNICA _ DATA-ENGINEER

Resolución de la prueba técnica para Data Engineer. Incluye ejercicios de Python orientado a objetos y DAGs en Apache Airflow

## 📂 ESTRUCUTRA DEL REPOSITORIO

```
de-tech-challenge/
├─ README.md
├─ python/
│  ├─ __init__.py
│  ├─ personas.py
│  └─ trabajador.py
└─ dags/
│  └─  test.py
├─ .env
└─ docker-compose.yaml

```

## 📌 NOTAS 

El archivo docker-compose.yaml se encontraba mi ruta de "Documents" en vez de en la carpeta del proyecto porque ya tenía Docker instalado previamente en esa ubicación. Queria evitar conflictos y reutilizar la instalación existente.

tambien adjunto el archivo .env con las variables necesarias (AIRFLOW_PROJ_DIR, AIRFLOW_IMAGE_NAME, etc.).

Por tanto he copiado el docker-compose.yaml y el .env a la estructura del proyecto en Visual Studio para que se visualice correctamente el archivo YAML y las variables de entorno asociadas, manteniendo el proyecto organizado y consistente con la configuración de Docker.