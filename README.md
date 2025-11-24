# Database Automation Helper

## 🎯 Objective

A simple Python utility designed to streamline interactions with SQL Server databases.  
This project provides a clean and reusable interface for connecting to a database, running queries, and performing CRUD (Create, Read, Update, Delete) operations using SQLAlchemy and PyODBC.

---

## 🚀 Features

- Automatic database connection using SQLAlchemy + PyODBC  
- Select data from any table  
- Insert new rows  
- Update existing rows  
- Delete rows with conditions  
- List all tables in the database  
- Secure configuration using environment variables  
- Automatic engine cleanup after each operation  

---

## 🛠 Technologies Used

- **Python**
- **SQLAlchemy**
- **PyODBC**
- **Pandas**
- **dotenv**
- **SQL Server**

---

## 🚀 Running the Project

pip install -r requirements.txt
Make a .env and put in there in this model
DATABASE_HOST = 'your connection name, like (DESKTOP_...)'
DATABASE_NAME = 'your database'