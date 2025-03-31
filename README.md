File Integrity Checker

🔹 Overview

A simple web app to:✔️ Upload and store file hashes✔️ Check file integrity✔️ Get alerts if files are modified

🔹 Technologies Used

Frontend: HTML, CSS, JavaScript, SweetAlert2

Backend: Flask (Python)

Database: PostgreSQL

🔹 Setup Instructions

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Database Setup

CREATE DATABASE file_integrity_checker;
CREATE TABLE file_hashes (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_hash TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3️⃣ Update Database Credentials in app.py

DATABASE_URL = "dbname=file_integrity_checker user=flask_user password=your_password host=localhost port=5432"

4️⃣ Run the Application

python app.py

Open http://127.0.0.1:5000/ in your browser.

🔹 Backup & Restore Database

To backup:

pg_dump -U flask_user -h localhost -p 5432 -d file_integrity_checker -F c -b -v -f backup.sql

To restore:

pg_restore -U flask_user -h localhost -p 5432 -d file_integrity_checker -v backup.sql

🔹 How It Works

1️⃣ Upload a file → The system saves its SHA-256 hash2️⃣ Check integrity → Compare current hash with the stored one3️⃣ ✅ Same hash → File is unchanged4️⃣ ❌ Different hash → File is modified

💻 Developed by Vaani 🚀

