#!/bin/bash

echo "[INFO] Waiting for Kafka Connect to be ready..."

until curl -s -o /dev/null -w '%{http_code}' http://localhost:8083/connectors | grep -q "200"; do
  echo "[INFO] Kafka Connect not ready yet. Sleeping..."
  sleep 5
done

echo "[INFO] Kafka Connect is ready. Registering connectors..."

echo "[INFO] Registering source connector..."
curl -X POST -H "Content-Type: application/json" \
  --data "@/init/source.json" \
  http://localhost:8083/connectors

echo "[INFO] Registering sink connector..."
curl -X POST -H "Content-Type: application/json" \
  --data "@/init/sink.json" \
  http://localhost:8083/connectors

echo "[INFO] Done."
