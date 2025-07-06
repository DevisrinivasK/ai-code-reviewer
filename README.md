CodeGuide AI
CodeGuide AI,  is a full-stack web application designed to assist developers in analyzing and improving their code. It provides four core features: error fixing, code optimization, plagiarism checking, and documentation generation for Python, Java, and C code. The application combines a modern, responsive frontend with a robust Flask backend, leveraging AI-powered analysis via the Google Gemini API, PostgreSQL for data persistence, and ReportLab for PDF generation.
Features

Code Error Fixer: Detects and corrects syntax, runtime, and logical errors in Python, Java, and C code using static analysis (ast, javalang, regex) and AI-driven fixes via Gemini API.
Code Optimizer: Improves code performance by applying rule-based optimizations (e.g., simplifying conditionals, enhancing loops) and AI-driven suggestions, with execution time metrics.
Code Plagiarism Checker: Identifies potential plagiarism by comparing code against common algorithm patterns (e.g., bubble sort, Fibonacci) and generates unique alternatives if needed.
Code Documentation Generator: Produces detailed documentation including problem statements, input/output formats, algorithms, and examples, with downloadable PDF reports.

Tech Stack

Frontend: HTML, CSS, JavaScript, Jinja2 (Flask templating), Font Awesome, Google Fonts (Orbitron, Inter)
Backend: Python, Flask
Libraries:
psycopg2: PostgreSQL database integration
google-generativeai: Google Gemini API for AI-driven analysis
reportlab: PDF generation for documentation
ast: Python code parsing
javalang: Java code parsing
hashlib, re, subprocess, logging: Additional utilities for analysis and logging


Database: PostgreSQL for storing analysis logs
External Tools: GCC (for C compilation), Java (for Java compilation)

Project Structure
CodeGuideAI/
├── app.py                  # Flask application and routes
├── test5.py               # Error-fixing logic
├── test7.py               # Code optimization logic
├── test8.py               # Plagiarism checking logic
├── test9.py               # Documentation generation logic
├── templates/
│   ├── index.html         # Home page
│   ├── fix_errors.html    # Error fixer page
│   ├── optimize.html      # Code optimizer page
│   ├── plagiarism.html    # Plagiarism checker page
│   ├── document.html      # Documentation generator page
├── README.md              # Project documentation

Prerequisites
To run CodeGuide AI locally, ensure you have the following installed:

Python: Version 3.8 or higher
PostgreSQL: Version 12 or higher, with a running server
Java: JDK 8 or higher (for Java code compilation)
GCC: For C code compilation
Git: For cloning the repository
pip: Python package manager
A Google Gemini API key (obtain from Google AI Studio)

Setup Instructions
Follow these steps to set up and run the project locally:
1. Clone the Repository
Clone the project from GitHub:
git clone https://github.com/YOUR_USERNAME/CodeGuideAI.git
cd CodeGuideAI

Replace YOUR_USERNAME with your GitHub username.
2. Set Up a Virtual Environment
Create and activate a Python virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
Install the required Python packages:
pip install flask psycopg2-binary google-generativeai reportlab javalang

4. Configure PostgreSQL
Ensure PostgreSQL is running and create a database named postgres:
psql -U postgres
CREATE DATABASE postgres;
\q

Verify the database connection settings in app.py, test5.py, test7.py, test8.py, and test9.py:
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",  # Update with your PostgreSQL password
    "host": "localhost",
    "port": "5432"
}

Update the password field if your PostgreSQL setup uses a different password.
5. Set Up Google Gemini API
Obtain a Gemini API key from Google AI Studio and update the GEMINI_API_KEY in app.py, test5.py, test7.py, test8.py, and test9.py:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Replace YOUR_GEMINI_API_KEY with your actual API key. For security, consider using environment variables (see below).
6. Set Up Environment Variables (Optional, Recommended)
To securely manage sensitive data, create a .env file in the project root:
touch .env

Add the following:
GEMINI_API_KEY=your_gemini_api_key
DB_PASSWORD=your_postgres_password

Install python-dotenv and update the Python files to load environment variables:
pip install python-dotenv

Modify each Python file (app.py, test5.py, test7.py, test8.py, test9.py) to include:
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

7. Verify External Tools
Ensure Java and GCC are installed:
java -version
gcc --version

Install them if missing:

Java: Install JDK (e.g., OpenJDK or Oracle JDK).
GCC: Install via sudo apt install gcc (Linux), brew install gcc (macOS), or MinGW (Windows).

8. Run the Application
Start the Flask development server:
python app.py

The application will be available at http://127.0.0.1:5000.
Usage

Access the Application:

Open http://127.0.0.1:5000 in your browser.
The home page (index.html) provides navigation to all features.


Features:

Code Error Fixer (/fix-errors): Paste code, select a language (Python, Java, C), and click "Fix Errors" to get corrected code and error analysis.
Code Optimizer (/optimize): Paste code, select a language, and click "Optimize Code" to receive optimized code with performance metrics.
Code Plagiarism Checker (/check-plagiarism): Paste code, select a language (python, java, c), and click "Check Plagiarism" to get a plagiarism score and alternative code if needed.
Code Documentation (/document): Paste code, select a language, and click "Generate Documentation" to view documentation or "Download PDF" for a PDF version.


Interacting with the UI:

Use the toolbar buttons to paste code, copy input/output, or download results.
Switch between dark and light themes using the theme toggle button.
The analysis area displays detailed reports, including error counts, execution times, plagiarism scores, or documentation success messages.



Database Schema
The application uses PostgreSQL to store analysis logs in the following tables:

code_analysis_logs (error fixing): Stores language, original code, corrected code, error report, error count, and timestamp.
code_optimization_records (optimization): Stores language, original code, optimized code, debug info, execution time, optimization level, and timestamp.
code_plag (plagiarism): Stores language, original code, cleaned code, plagiarism score, analysis, and timestamp.
code_doc_logs (documentation): Stores language, original code, documentation, and timestamp.



License
This project is licensed under the MIT License.
