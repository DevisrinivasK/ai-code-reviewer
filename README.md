# CodeGuide AI

**AI-Powered Code Review and Documentation Tool**

---

## 1. Project Overview

CodeGuide AI is a full-stack web application designed to assist developers in analyzing and improving their code. It provides four core features: error fixing, code optimization, plagiarism checking, and documentation generation for Python, Java, and C code.

The application combines a modern, responsive frontend with a robust Flask backend, leveraging AI-powered analysis via the Google Gemini API, PostgreSQL for data persistence, and ReportLab for PDF generation.

The project automates repetitive code review tasks, ensuring developers can:

- Detect and fix errors in code.
- Optimize code for performance and readability.
- Check for plagiarism and generate unique alternatives.
- Produce professional documentation with downloadable PDFs.

This eliminates manual effort, improves code quality, and enhances productivity for solo developers and teams alike.

---

## 2. Features

The project includes the following key features:

### 2.1 Code Error Fixer

Detects and corrects syntax, runtime, and logical errors in Python, Java, and C code using static analysis (ast, javalang, regex) and AI-driven fixes via the Gemini API. Provides detailed error reports and corrected code.

### 2.2 Code Optimizer

Improves code performance by applying rule-based optimizations (e.g., simplifying conditionals, enhancing loops) and AI-driven suggestions. Includes execution time metrics to quantify improvements.

### 2.3 Code Plagiarism Checker

Identifies potential plagiarism by comparing code against common algorithm patterns (e.g., bubble sort, Fibonacci). Generates unique alternative implementations if plagiarism is detected (score >20%).

### 2.4 Code Documentation Generator

Produces detailed documentation including problem statements, input/output formats, algorithms, and examples. Outputs professional PDF reports using ReportLab for easy sharing and archiving.

---

## 3. Tech Stack

The project leverages a modern tech stack for robust functionality:

### 3.1 Frontend

- HTML, CSS, JavaScript: For building interactive web pages.
- Jinja2: Flask templating for dynamic content rendering.
- Font Awesome: For icons in the user interface.
- Google Fonts (Orbitron, Inter): For typography

### 3.2 Backend

- Python: Core programming language.
- Flask: Web framework for routing and rendering.

### 3.3 Libraries

- psycopg2: PostgreSQL database integration.
- google-generativeai: Google Gemini API for AI-driven analysis.
- reportlab: PDF generation for documentation.
- ast: Python code parsing.
- javalang: Java code parsing.
- hashlib, re, subprocess, logging: Utilities for analysis and logging.

### 3.4 Database

- PostgreSQL: For storing analysis logs.

### 3.5 External Tools

- GCC: For C code compilation.
- Java: For Java code compilation.

---

## 4. Project Structure

The project is organized as follows:

![image](https://github.com/user-attachments/assets/36527d42-4f4a-45f8-a347-7767a7676a1e)

---

## 5. Prerequisites

To run CodeGuide AI locally, ensure the following are installed:

- Python: Version 3.8 or higher.
- PostgreSQL: Version 12 or higher, with a running server.
- Java: JDK 8 or higher (for Java code compilation).
- GCC: For C code compilation.
- Git: For cloning the repository.
- pip: Python package manager.
- Google Gemini API key: Obtain from Google AI Studio.

---

## 6. Setup Instructions

Follow these steps to set up and run the project locally:

### 6.1 Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/DevisrinivasK/ai-code-reviewer.git
cd CodeGuideAI

# Code Analysis Web Application

## 6.2 Set Up a Virtual Environment
Create and activate a Python virtual environment:

```bash
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Code Analysis & Optimization Web App

## 6.3 Install Dependencies

Install the required Python packages:

```bash
pip install flask psycopg2-binary google-generativeai reportlab javalang python-dotenv

## 6.4 Configure PostgreSQL

Ensure PostgreSQL is running and create a database named postgres:

```bash
psql -U postgres
CREATE DATABASE postgres;
\q
Verify the database connection settings in app.py, test5.py, test7.py, test8.py, and test9.py:
DB_PARAMS = {
  "dbname": "postgres",
  "user": "postgres",
  "password": "your_postgres_password",
  "host": "localhost",
  "port": "5432"
}
## 6.5 Set Up Google Gemini API

Obtain a Gemini API key from Google AI Studio and update the `GEMINI_API_KEY` in `app.py`, `test6.py`.
## 6.6 Set Up Environment Variables (Recommended)

Create a `.env` file in the project root:

```bash
touch .env
Add the following:
GEMINI_API_KEY=your_gemini_api_key
DB_PASSWORD=your_postgres_password
Install python-dotenv:
pip install python-dotenv
Modify each Python file to load environment variables:
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DB_PARAMS = {
  "dbname": "postgres",
  "user": "postgres",
  "password": os.getenv("DB_PASSWORD"),
  "host": "localhost",
  "port": "5432"
}
## 6.7 Verify External Tools

Ensure Java and GCC are installed:

```bash
java -version  
gcc --version
Install if missing:

Java: Install JDK (e.g., OpenJDK or Oracle JDK)

GCC:

Linux: sudo apt install gcc

macOS: brew install gcc

Windows: Use MinGW
## 6.8 Run the Application

Start the Flask development server:

```bash
python app.py
The application will be available at http://127.0.0.1:5000.
## 7.1 Access the Application

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. The home page (`index.html`) provides navigation to all features.
## 7.2 Features

- **Code Error Fixer** (`/fix-errors`):  
  Paste code, select a language (Python, Java, C), and click "Fix Errors" to get corrected code and error analysis.

- **Code Optimizer** (`/optimize`):  
  Paste code, select a language, and click "Optimize Code" to receive optimized code with performance metrics.

- **Code Plagiarism Checker** (`/check-plagiarism`):  
  Paste code, select a language, and click "Check Plagiarism" to get a plagiarism score and alternative code if needed.

- **Code Documentation** (`/document`):  
  Paste code, select a language, and click "Generate Documentation" to view documentation or "Download PDF" for a PDF version.
## 7.3 Interacting with the UI

- Use toolbar buttons to paste code, copy input/output, or download results.
- Switch between dark and light themes using the theme toggle button.
- The analysis area displays detailed reports, including error counts, execution times, plagiarism scores, or documentation success messages.
## 8 Database Schema

The application uses PostgreSQL to store analysis logs in the following table:

**`codeanalysislogs` (errorfixing):**  
Stores language, original code, corrected code, error report, error count
## 9 License

This project is licensed under the MIT License:

- You are free to use, modify, and distribute the code.
- The project comes with no warranties, and contributors are not liable for issues arising from its use.
- Check the full MIT License text for details if redistributing the project.


