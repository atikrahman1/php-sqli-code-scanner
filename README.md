# PHP SQL Injection Auditor

This Python script scans PHP files for potential SQL injection vulnerabilities. It identifies variables from `$_GET`, `$_POST`, and `$_REQUEST` superglobals and checks if they are used in SQL queries without proper sanitization.

## Features
- Scans directories recursively for PHP files.
- Detects variables derived from `$_GET`, `$_POST`, and `$_REQUEST`.
- Checks for SQL queries that use these variables without sanitization via `mysqli_real_escape_string` or `mysql_real_escape_string`.
- Highlights the file path, variable name, and line number of potential vulnerabilities.

## How It Works
1. The script uses regular expressions to identify:
   - Variables defined from superglobals (`$_GET`, `$_POST`, `$_REQUEST`).
   - SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
2. It verifies if the identified variables are sanitized before being used in the SQL query.
3. Outputs detailed information about any potential vulnerabilities.

## Prerequisites
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/php-sql-injection-auditor.git
   cd php-sql-injection-auditor
