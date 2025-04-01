# Vital Signs Monitoring System

This project provides a comprehensive setup for monitoring vital signs using technologies like Docker, Kubernetes, Kafka, and Snowflake.

## Project Structure

- **data**: Contains placeholder CSV files for vital signs data.
- **docker**: Docker setup for local testing, including PostgreSQL and a consumer app.
- **sql**: SQL scripts for querying and exporting data.
- **kafka**: Kafka producer and connector configuration.
- **kubernetes**: Kubernetes manifests for deploying the system.
- **snowflake**: Scripts for loading and querying data in Snowflake.

## Getting Started

### Prerequisites

- Docker
- Kubernetes
- Kafka
- Snowflake account

### Setup Instructions

1. **Docker and Kubernetes Setup**:
   - Ensure Docker and Kubernetes are installed and running on your machine.

2. **Start Services**:
   - Use `docker-compose` to start the necessary services. This will set up the environment with PostgreSQL and the consumer app.

3. **Deploy to Kubernetes**:
   - Deploy the Kubernetes manifests located in the `kubernetes` directory to set up the system in a Kubernetes cluster.

4. **Kafka Setup**:
   - Use the Kafka producer script in the `kafka` directory to send data to the Kafka topic.

5. **Data Querying**:
   - Use the SQL scripts in the `sql` directory or the Snowflake scripts in the `snowflake` directory to query and analyze the data.

## Detailed Components

### Docker

- **docker-compose.yml**: Defines the services for local development and testing.
- **Kafka Configuration**: Located in `docker/kafka`, includes Kafka connectors and initialization scripts.

### Kafka

- **Producer**: `producer.py` sends data to Kafka topics.
- **Consumer**: `consumer.py` reads data from Kafka topics.

### Kubernetes

- **Manifests**: YAML files for deploying services like Kafka, Zookeeper, PostgreSQL, SQL Server, and the consumer app.

### Snowflake

- **Scripts**: `load_and_query.sql` for loading data into Snowflake and running queries.

### SQL

- **Scripts**: Includes `create_tables.sql` for table creation, `export.sql` for data export, and `queries.sql` for running queries.
