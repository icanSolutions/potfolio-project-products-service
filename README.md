# 🧱 Products Service

This is a lightweight **Flask microservice** that manages product data in a cloud-native architecture. It’s part of a broader system designed to demonstrate DevOps practices using microservices.

## 📦 Features

- CRUD operations for products
- RESTful API with JSON responses
- Built with Flask
- Tested using Pytest and BDD (pytest-bdd)

## 🛠 Tech Stack

- Python 3
- Flask
- Pytest & pytest-bdd
- Docker

## 📂 Project Structure

products-service/
│
├── app/                  # Flask application code
│   ├── init.py
|   ├── run.py
|   ├── config.py
|   ├── errors.py
|   ├── models.py
|   ├── schema.py
│   └── routes.py
├── tests/                # Unit and BDD tests
│   ├── test_routes.py
│   ├── test_product_bdd.py
│   ├── factories.py
│   └── features/
├── utils/                # Unit and BDD tests
│   ├── db_helpers.py
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── setup.sh
└── README.md

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repo_url>
cd products-service

### 2. Setup

```bash
bash setup.sh
