
---

# **🏪 CircuitCart - E-commerce Website for Computer Components & Peripherals**  

Welcome to **CircuitCart**, an e-commerce platform designed for selling **computer components** and **peripherals**. This website consists of a **Django backend** with a **PostgreSQL database** and a **React frontend**, making it a powerful full-stack application.

---

## **📌 Features**
✅ **Modern Frontend:** Built with **React.js** and styled for a smooth user experience.  
✅ **Robust Backend:** Developed using **Django REST Framework (DRF)** and **PostgreSQL**.  
✅ **Product Management:** Displays components and peripherals dynamically from the database.  
✅ **API-Driven Architecture:** RESTful APIs for seamless frontend-backend communication.  
✅ **User Authentication:** Supports **Login, Registration, and Secure Authentication**.  
✅ **Payment Integration:** Ready for **Stripe and PayPal** integration.  
✅ **Mobile-Friendly & Responsive:** Optimized for all devices.  

---

## **🛠 Tech Stack**
### **Frontend:**
- **React.js** (JavaScript framework)
- **React Router** (for navigation)
- **Fetch API / Axios** (for API requests)
- **Bootstrap / Tailwind CSS** *(Optional, for styling)*

### **Backend:**
- **Django** (Python web framework)
- **Django REST Framework** (for API development)
- **PostgreSQL** (Database)
- **JWT Authentication / Django Auth** (for user authentication)

---

## **📂 Folder Structure**
```
CircuitCart/
├── backend/            # Django backend
│   ├── ecommerce/      # Main Django project folder
│   ├── store/          # Django app (Products & API)
│   ├── env/            # Virtual environment (Python)
│   ├── manage.py       # Django management file
│   ├── db.sqlite3      # Default SQLite DB (if PostgreSQL is not configured)
│   ├── requirements.txt # Python dependencies
│
├── frontend/           # React frontend
│   ├── src/            # React source code
│   │   ├── components/ # Reusable UI components
│   │   ├── pages/      # Different website pages
│   │   ├── assets/     # Images, logos, etc.
│   │   ├── App.js      # Main React App component
│   │   ├── index.js    # Entry point for React
│   │   ├── styles.css  # Global styles
│   ├── public/         # Static public files
│   ├── package.json    # Frontend dependencies
│
└── README.md           # This file!
```

---

## **🚀 Installation & Setup**
Follow these steps to set up **CircuitCart** on your local machine.

### **1️⃣ Prerequisites**
Before starting, make sure you have installed:
- **Python 3.7+** (for Django)
- **Node.js & npm** (for React)
- **PostgreSQL** (for database)
- **PowerShell (Windows) / Terminal (Mac/Linux)**

---

## **📌 Backend Setup (Django + PostgreSQL)**

### **1️⃣ Set Up the Backend**
```powershell
cd CircuitCart
mkdir backend
cd backend
python -m venv env
.\env\Scripts\Activate.ps1   # Windows
# source env/bin/activate    # Mac/Linux
```

### **2️⃣ Install Dependencies**
```powershell
pip install django djangorestframework psycopg2-binary
```

### **3️⃣ Create the Django Project & App**
```powershell
django-admin startproject ecommerce .
python manage.py startapp store
```

### **4️⃣ Configure Database (PostgreSQL)**
In **`ecommerce/settings.py`**, replace the `DATABASES` section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **5️⃣ Apply Migrations & Create Superuser**
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin account
```

### **6️⃣ Run the Django Development Server**
```powershell
python manage.py runserver
```
🚀 **Your API will be available at:** `http://127.0.0.1:8000/api/products/`

---

## **📌 Frontend Setup (React.js)**
### **1️⃣ Set Up the Frontend**
```powershell
cd CircuitCart
mkdir frontend
cd frontend
npx create-react-app ecommerce-frontend
cd ecommerce-frontend
npm install react-router-dom
```

### **2️⃣ Start the React Development Server**
```powershell
npm start
```
🚀 **Your React App will be available at:** `http://localhost:3000/`

---

## **🔌 Connecting Frontend & Backend**
### **1️⃣ Proxy API Requests**
In **`frontend/package.json`**, add:
```json
"proxy": "http://127.0.0.1:8000"
```
This ensures that frontend API calls (`fetch('/api/products')`) are redirected to Django.

---

## **🌟 API Endpoints**
| Method | Endpoint                | Description               |
|--------|-------------------------|---------------------------|
| `GET`  | `/api/products/`        | Fetch all products       |
| `GET`  | `/api/products/featured/` | Fetch featured products |
| `GET`  | `/api/products/combos/` | Fetch combo deals       |
| `POST` | `/api/products/add/`    | Add new product (Admin)  |
| `POST` | `/api/register/`        | Register new user        |
| `POST` | `/api/login/`           | Authenticate user        |

---

## **💳 Payment Integration (Stripe & PayPal)**
💰 **For Payments**, we will integrate **Stripe & PayPal**:
1. **Install Stripe SDK**
   ```powershell
   npm install @stripe/react-stripe-js @stripe/stripe-js
   ```
2. **Configure Stripe API Key in React**
   ```javascript
   import { loadStripe } from '@stripe/stripe-js';

   const stripePromise = loadStripe("your_public_key_here");
   ```

🔹 **More details will be provided in future updates!**

---

## **📢 Contributing**
Want to improve **CircuitCart**? Feel free to contribute:
1. Fork this repo
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Add new feature"`
4. Push: `git push origin feature-branch`
5. Create a **Pull Request (PR)**

---

## **📜 License**
**CircuitCart** is licensed under the **MIT License**. Feel free to use and modify it!

---