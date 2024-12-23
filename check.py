import re
import os

# Directory containing PHP files
php_files_dir = "C:/Users/Desktop/php-project"  # Update to your directory

# ANSI escape codes for red text
RED_COLOR = "\033[91m"
YELLOW_COLOR ="\033[93m"
RESET_COLOR = "\033[92m"

# Regular expressions to match $_GET, $_POST, and $_REQUEST variables
pattern_variables = re.compile(r'\$(\w+)\s*=\s*\$_(GET|POST|REQUEST)\s*\[\s*[\'"](\w+)[\'"]\s*\];')
# Regular expression to match SQL queries
pattern_sql_injection = re.compile(r'\b(select|insert|update|delete)\b.*?;', re.IGNORECASE | re.DOTALL)

# Function to check for SQL injection vulnerabilities
def check_sql_injection(file_path):
    vulnerabilities = []
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
        # Step 1: Identify variables from $_GET, $_POST, $_REQUEST
        defined_variables = pattern_variables.findall(content)
        defined_var_names = {var[0] for var in defined_variables}  # Extract just the variable names
        
        # Step 2: Check for SQL queries that use these variables without sanitization
        for line_number, line in enumerate(content.splitlines(), start=1):
            if pattern_sql_injection.search(line):
                for var_name in defined_var_names:
                    if f"${var_name}" in line and not re.search(rf'mysqli_real_escape_string\s*\(.*?\${var_name}.*?\)|mysql_real_escape_string\s*\(.*?\${var_name}.*?\)', line):
                        vulnerabilities.append((var_name, line_number))
                        # print(f"{RED_COLOR}Vulnerability found: ${var_name} on line {line_number}{RESET_COLOR}")

    return vulnerabilities

# Analyze each PHP file in the specified directory
def analyze_php_files():
    for root, dirs, files in os.walk(php_files_dir):
        for file in files:
            if file.endswith(".php"):
                file_path = os.path.join(root, file)
                vulnerabilities = check_sql_injection(file_path)
                
                if vulnerabilities:
                    print(f"\nFile: {YELLOW_COLOR}{file_path}")
                    for var_name, line_number in vulnerabilities:
                        print(f"{RED_COLOR}Potential SQL injection vulnerability found.")
                        print(f"Variable: ${var_name} on line: {line_number}{RESET_COLOR}")
                else:
                    print(f"File: {file_path} - No vulnerabilities found.")

# Run the script
analyze_php_files()
