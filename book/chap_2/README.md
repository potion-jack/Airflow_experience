# Airflow

## by python

```
1.
> airflow db init

2.
> airflow users create
--username admin
--password admin
--firstname Anonymous
--lastname Admin
--role Admin
--email addmin@example.org

3. cp download_rocket_launches.py ~/airflow/dags/

4. airflow webserver

5. airflow scheduler

```

## by docker

```
docker run \
-ti \
-p 8080:8080 \
-v ~/airflow/dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py \
--name airflow_2 \
--entrypoint=/bin/bash \
apache/airflow:2.0.0-python3.8 \
-c '( \
airflow db init && \
airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org \
); \
airflow webserver & \
airflow scheduler \
'
```
