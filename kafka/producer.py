from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Example data
vital_sign = {
    'patient_id': 1,
    'heart_rate': 72,
    'blood_pressure': '120/80',
    'temperature': 36.6
}

producer.send('vital_signs', vital_sign)
producer.flush()
