# Data Engineering Project - Latest Games from Rawg.io API

[![Screen-Shot-2023-07-26-at-20-54-11.png](https://i.postimg.cc/6QY94GKF/Screen-Shot-2023-07-26-at-20-54-11.png)](https://postimg.cc/f3S46yJv)

## Objectives
This is a data engineering project that focuses on analyzing the latest six months of game data from the website Rawg.io using their provided API. The data obtained from the API is then processed and stored in a MySQL database. The data stored in the database is then used for data analysis using Tableau.

## Project architecture
[![Project-Diagram.png](https://i.postimg.cc/SK0tqydF/Untitled-Diagram.png)](https://postimg.cc/pmZBJM3q)
- Data Source: API [Rawg.io](https://rawg.io/)
- Data Lake: Local Storage, saved as JSON files
- Data Transformation: Python with Pandas
- Data Warehouse: MySQL
- Data Visualization: Tableau
- Workflow Management: Apache Airflow

## Result - Data Visualization
TBA

## Setup and Running
### Setting up and Activating the Virtual Environment
Set up a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) and install the required version of Python. Don't forget to create a new venv.
```
pyenv install 3.8.10
pyenv virtualenv 3.8.10 airflow
pyenv activate airflow
```
### Installing Apache Airflow
Install Apache Airflow by following the instructions in the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html).  I used Airflow version `2.6.3`.
### Installing requirements.txt
```
pip install -r requirements.txt
```
### Make sure MySQL is installed
Make sure MySQL is installed. Then, don't forget to change the database configuration in the `load_data_to_db.py` file according to the MySQL configuration on your computer.
```
# Define the MySQL database connection parameters
host = 'CHANGE'
user = 'CHANGE'
password = 'CHANGE'
database = 'rawg_db'
```
### Run pipelines
1. Make sure Airflow is running smoothly.
2. Move the contents of the `dags` folder in this repository to the `dags` folder in your Airflow installation.
```
cp -a dags/ $AIRFLOW_HOME/dags/
```
3. Open the Airflow UI and activate the `rawg_etl` DAG.
4. Wait until the DAG has finished running.

## Future Work
- [ ] Packaging all ETL processes using Docker
- [ ] Tidying up data in the Data Warehouse using dbt
- [ ] Building infrastructure using Terraform