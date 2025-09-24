# PRUEBA-TÉCNICA

Resolución de la prueba técnica para Data Engineer. Incluye ejercicios de Python orientado a objetos y DAGs en Apache Airflow

## 📂 Estructura básica del repositorio  

```
de-tech-challenge/
├─ README.md
├─ python/
│  └─ personas.py
└─ dags/
   ├─ test_dag.py


---

## 1) Ejercicio Python – POO (`python/personas.py`)  

**Qué se demuestra**  
- Herencia (`Trabajador` hereda de `Persona`).  
- Uso correcto de `__init__`, con valores por defecto (`departamento="Data"`, `puesto="Analyst"`).  
- Sobrescritura de método (`presentation`), manteniendo la funcionalidad original con `super()`.  
- Creación de instancias desde una **lista** (`*args`) y desde un **diccionario** (`**kwargs`).  
- Explicación de la diferencia entre `self.nombre` (atributo del objeto) y `nombre` (variable local).  

**Ejecutar el script**  

```bash
cd python
python personas.py
```

Se imprimirán las presentaciones de las distintas instancias.  

---

## 2) Ejercicio Airflow (`airflow/dags/test_dag.py`)  

**Qué se demuestra**  
- DAG en Airflow 2.x con ejecución diaria a las **03:00 UTC** (`0 3 * * *`).  
- Flujo de dependencias: `start` → lista de `task_n` → `timediff` → `end`.  
- Cada tarea **par** depende de **todas las impares** (fan-in).  
- Operador personalizado `TimeDiffOperator` que:  
  - Recibe una fecha (`str` o `datetime`).  
  - Calcula y muestra en logs la diferencia con la fecha actual.  
- Comentario que explica la diferencia entre **Connection** y **Hook** en Airflow.  

---

## 🚀 Ejecución rápida con Docker (recomendado)  

**Requisitos**: Docker y Docker Compose.  

```bash
cd airflow
docker compose up -d

# Inicialización (ejecutar una sola vez)
docker compose exec airflow-webserver airflow db init
docker compose exec airflow-webserver airflow users create   --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Reiniciar servicios
docker compose restart
```

Abrir Airflow en **http://localhost:8080** con user/pass `admin`/`admin`.  
Habilitar el DAG `test` y lanzarlo.  

---

## 🖥️ Ejecución en local (sin Docker)  

**Requisitos**: Python 3.10+  

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Configuración mínima
export AIRFLOW_HOME="$(pwd)/.airflow_home"
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Arrancar Airflow
airflow webserver --port 8080 &
airflow scheduler
```

Abrir http://localhost:8080, habilitar el DAG `test` y ejecutarlo.  

---

## ✅ Sugerencia de commits  

- `python: añadir clases Persona/Trabajador`  
- `python: sobrescribir presentation y añadir valores por defecto`  
- `python: instancias desde lista y diccionario`  
- `airflow: DAG de prueba con dependencias`  
- `airflow: operador personalizado TimeDiff`  
- `docs: añadir README y quickstart`  

---

## 📌 FAQ – Puntos de razonamiento esperados  

- **`self.nombre` vs `nombre`**:  
  - `self.nombre` es un atributo ligado al estado de la instancia.  
  - `nombre` es una variable local al ámbito actual.  

- **Airflow Connection vs Hook**:  
  - Una *Connection* es la configuración (host, user, password, etc.) guardada en el metastore.  
  - Un *Hook* es una clase que usa esa *Connection* para abrir la conexión real y ejecutar operaciones (ej. `S3Hook`, `PostgresHook`).  

- **Dependencia pares/impares**: demuestra lógica para generar dependencias dinámicas en DAGs.  

- **Custom Operator**: demuestra herencia desde `BaseOperator`, manejo de argumentos, logging y return.  
