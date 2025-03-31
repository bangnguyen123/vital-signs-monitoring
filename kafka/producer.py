from confluent_kafka import Producer
import csv
import time
import json

p = Producer({'bootstrap.servers': 'kafka:9092'})

with open('/data/mhealth_vital_signs.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # message = {
        #     "patient_id": int(row['patient_id']),
        #     "timestamp": row['timestamp'],
        #     "heart_rate": int(row['heart_rate'])
        # }
        message = {
            "schema": {
                "type": "struct",
                "fields": [
                {"field": "patient_id", "type": "int32"},
                {"field": "timestamp", "type": "string"},
                {"field": "heart_rate", "type": "int32"}
                ],
                "optional": False,
                "name": "vital_signs"
        },
        "payload": {
            "patient_id": int(row['patient_id']),
            "timestamp": row['timestamp'],
            "heart_rate": int(row['heart_rate'])
        }
        }
        p.produce('vital_signs', value=json.dumps(message).encode('utf-8'))

        # p.produce('vital_signs', value=json.dumps(message).encode('utf-8'))
        print(f"Produced: {message}")
        time.sleep(1)
        p.flush()
print("Streaming complete!")