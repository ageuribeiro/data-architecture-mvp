FROM apache/airflow:2.7.1-python3.11

# Copiar seus DAGS
COPY dags/ $AIRFLOW_HOME/dags/

# Copiar outros scripts, se precisar
COPY scripts/ $AIRFLOW_HOME/scripts/

# Instalar bibliotecas extras (Pandas, NumPy, etc.)
USER root
RUN pip install --no-cache-dir pandas numpy pyarrow
USER airflow

