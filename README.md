# 🐳 Dockerized User Feedback Application

## 📌 Project Overview
This project is a fully containerized **User Feedback Web Application** built using:

- Flask (Python Backend API)
- PostgreSQL Database
- HTML, CSS, JavaScript Frontend
- Docker & Docker Compose for container orchestration

Users can submit feedback via a web interface, and all feedback is stored persistently in a PostgreSQL database using Docker volumes.

---

## 🏗️ Architecture Overview

Browser → Frontend (Nginx) → Backend (Flask API) → PostgreSQL Database  
All services communicate over a custom Docker network.

---

## 🐳 Docker Components

### 1. Backend (Flask API)
- Custom Dockerfile based on Python image
- Handles POST and GET requests for feedback

### 2. PostgreSQL Database
- Official PostgreSQL Docker image
- Uses Docker volume for persistent storage

### 3. Frontend (Nginx)
- Static HTML/CSS/JS served via Nginx container

---

## 📂 Project Structure

user-feedback-docker/
│
├── backend/
├── frontend/
├── docker-compose.yml
├── .env
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YomiHubHub/user-feedback-docker.git
cd user-feedback-docker

docker compose up -d --build

frontend:
http://localhost:8080
backend:
http://localhost:5000/feedback
