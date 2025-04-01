## I just want to track what i faced and how i fix it

### 1. I want to learning data engineering so i asked Grok to give some ideas about a small project and it gave me this idea regarding to the domain that i am working on Healthcare
### 2. I want to use Docker for running everything in this project and Kube for deployment

### 3. Do it:
- I created a docker-compose.yml file to define and start postgres, sqlserver, kafka, consumer and producer

- At the very begining, the producer read the csv file then write to kafka then nothing else happen

- It digged around and findout that the jdbc is not navtive installed in the kafka-connect image so I accessed to that container then run `confluent-hub install confluentinc/kafka-connect-jdbc:latest`

- But when i do the `curl -s http://localhost:8083/connector-plugins | jq` then i just see the mirror connector -> i restared the container then i can see the jdbc connector

- After that i realised that my `sink.json` does not work well so i need to update it to connect to sqlserver. Then I need to manually run `curl -X POST -H "Content-Type: application/json" --data @/init/sink.json http://localhost:8083/connectors`

- After this the task in sink just keeping failed but still because the format of message I need to rewrite the producer to send a message as current format and in sink we need to choose to use JsonConverter

- But if you notice above i gotta install the jdbc connect manualy so i decided to build a custome image for kafka connect. and I spend a afternoon to figure out why the image does not load the plugins correctly (because of the path. hic)

- The sqlserver image that i am using is a edge image from azure and there is no sql command to run inside the container. So, i download BeeKeeper to connect to sqlserver and create the database and table manually, then test the flow. It worked!. But i need docker to create the database and tables at the start So i create a init script for sqlserver and build a custome docker image for that.
