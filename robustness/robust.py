import os
import re

def analyze_robustness(directory):
    total_files_analyzed = 0
    total_try_except_blocks = 0
    total_specific_exceptions = 0
    total_error_messages = 0
    total_logging_statements = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    lines = f.readlines()
                    try_except_blocks = 0
                    specific_exceptions = 0
                    error_messages = 0
                    logging_statements = 0
                    for line in lines:
                        if "try" in line and "except" in line:
                            try_except_blocks += 1
                            match = re.search(r'except\s+(\w+)', line)
                            if match:
                                specific_exceptions += 1
                        if "logging" in line:
                            logging_statements += 1
                        if "except" in line and 'as' in line:
                            error_messages += 1

                    total_try_except_blocks += try_except_blocks
                    total_specific_exceptions += specific_exceptions
                    total_logging_statements += logging_statements
                    total_error_messages += error_messages
                    total_files_analyzed += 1

    print(f"Total Python files analyzed: {total_files_analyzed}")
    print(f"Total try-except blocks found: {total_try_except_blocks}")
    print(f"Total specific exceptions caught: {total_specific_exceptions}")
    print(f"Total error messages found: {total_error_messages}")
    print(f"Total logging statements found: {total_logging_statements}")

if __name__ == "__main__":
    directory = input("Enter the directory path to analyze: ")
    analyze_robustness(directory)

