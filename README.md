


# Digital Transformation in Banking - Complete Fraud Analysis System

## Overview
This system integrates AI-driven rule validation, Kafka for real-time streaming, and a dashboard for visualization.

## Modules
1. **backend**: Flask API for rule validation.
2. **frontend**: Dash dashboard for visualization.
3. **kafka**: Producer and consumer for streaming business rules.

## Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Pip

## Setup Instructions

### Backend
1. Navigate to the backend folder:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

### Frontend
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   pip install -r requirements.txt
   python dashboard.py
   ```

### Kafka
1. Navigate to the kafka folder and start Kafka services:
   ```bash
   docker-compose up -d
   ```
2. Run the producer:
   ```bash
   python kafka_producer.py
   ```
3. Run the consumer:
   ```bash
   python kafka_consumer.py
   ```

## Access the Application
- **Backend API**: `http://127.0.0.1:5000`
- **Dashboard**: `http://127.0.0.1:8050`
