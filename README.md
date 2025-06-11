# Advance Containers Assignment – Flask API with MySQL (Dockerized)

This project is a Dockerized web application that provides a REST API to create and fetch user data using a MySQL database. It follows DevOps best practices and optionally supports public internet access using a Cloudflare Tunnel.

---

## 📦 Features

- Simple Flask API (`POST /user`, `GET /user/<id>`)
- MySQL database container with volume persistence
- Docker Compose for orchestration
- Environment-based configuration
- Optional: Secure public exposure via Cloudflare `.trycloudflare.com` tunnel

---

## 🛠️ Tech Stack

- Python 3.10 (Flask)
- MySQL 8.0
- Docker & Docker Compose

---

## 📁 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── README.md
└── webapi/
    ├── app.py
    └── requirements.txt
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository (if needed)

```bash
git clone https://github.com/your-username/advance-containers-assignment.git
cd advance-containers-assignment
```

### 2. Start the Containers

```bash
docker-compose up --build
```

### 3. Test API Endpoints

#### ➕ Create User

```bash
curl -X POST http://localhost:5000/user -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe"}'
```

#### 🔍 Get User by ID

```bash
curl http://localhost:5000/user/1
```

---

## 🌐 Optional: Expose via Cloudflare Tunnel

You can use a free `.trycloudflare.com` URL to make the API publicly accessible.

### 1. Run the Tunnel

```bash
docker run -it --network host cloudflare/cloudflared:latest tunnel --url http://localhost:5000
```

> You will get a public URL like: `https://random-name.trycloudflare.com`

### 2. Test Public Access

```bash
curl https://random-name.trycloudflare.com/user/1
```

✅ No domain, firewall, or public IP needed!

---

## 🔐 Security Best Practices Applied

- Non-root base image (`python:3.10-slim`)
- Secrets via environment variables
- Internal-only networking with Docker
- Volume-based DB persistence

---

## 📜 License

MIT License. Free to use for educational purposes.

