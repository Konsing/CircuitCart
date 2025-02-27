# 🛒 CircuitCart

CircuitCart is a modern e-commerce platform dedicated to providing a wide range of computer components, peripherals, and more. Built with user experience and scalability in mind, CircuitCart offers a seamless shopping experience for tech enthusiasts, DIY builders, and professionals alike.

---

## Table of Contents
- [🚀 Project Overview](#project-overview)
- [✨ Features](#features)
- [🔧 Tech Stack](#tech-stack)
- [☁️ AWS Infrastructure](#aws-infrastructure)
- [⚙️ Environment Variable Templates](#environment-variable-templates)
- [🛠️ Development Considerations](#development-considerations)
- [🚀 Installation & Setup](#installation--setup)

---

## 🚀 Project Overview
CircuitCart is a comprehensive online store that caters to the needs of customers looking for computer components and peripherals. The platform is designed for a smooth and secure shopping experience and is hosted on AWS using EC2 for server hosting and S3 for static asset management. This approach ensures high availability, scalability, and performance.

---

## ✨ Features
- **Intuitive User Interface:** Easy navigation and a clean design to enhance user experience.
- **Extensive Product Catalog:** A wide range of computer components, peripherals, and related accessories.
- **Secure Checkout:** Robust payment gateway integration for safe transactions.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Scalable Infrastructure:** Leveraging AWS services (EC2 & S3) to accommodate growth and ensure reliability.
- **Fast Load Times:** Efficient asset management with S3 for optimal performance.

---

## 🔧 Tech Stack
- **Frontend:** REACT
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Hosting:** AWS EC2 for server deployment and AWS S3 for static asset storage.

---

## ☁️ AWS Infrastructure
CircuitCart is deployed on Amazon Web Services, utilizing:
- **EC2:** For hosting the application server and managing backend operations.
- **S3:** For storing and delivering static assets such as images, stylesheets, and JavaScript files.
- *(Additional AWS services, like CloudFront or RDS, can be added if used in your project.)*

---

## ⚙️ Environment Variable Templates

For proper configuration of the application, create the following `.env` files in the respective directories:

### Frontend (.env)
```dotenv
REACT_APP_API_URL=
```

### Backend (.env)
```dotenv
SQLALCHEMY_DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

---

## 🛠️ Development Considerations
When developing locally, please note the following:
- **Configuration Files:** Update `main.py` and `nginx.conf` to reflect your local development environment. These files should be adjusted when transitioning from local testing to production deployment.
- **Environment Settings:** Ensure that the settings in your `.env` files match your current environment, and double-check configurations before pushing to production.
- **Docker Command (Local Testing):**
   To run the full stack using Docker Compose, use the following command:
   ```bash
   docker-compose up -build
   ```
   This will start both the backend and frontend services in Docker containers.
   
---
