import os
import pycodestyle

def count_lines_of_code(directory):
    total_lines = 0
    total_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    lines = f.readlines()
                    total_lines += len(lines)
                    total_files += 1

    return total_files, total_lines

def analyze_code_quality(directory):
    num_files, num_lines = count_lines_of_code(directory)
    print(f"Total Python files found: {num_files}")
    print(f"Total lines of Python code: {num_lines}")

    # Check PEP 8 compliance
    style_guide = pycodestyle.StyleGuide()
    report = style_guide.check_files([directory])
    print(f"PEP 8 issues found: {report.total_errors}")

    # Calculate average lines of code per file
    if num_files > 0:
        avg_lines_per_file = num_lines / num_files
        print(f"Average lines of code per file: {avg_lines_per_file:.2f}")

    # Calculate average function and class lengths
    total_functions = 0
    total_classes = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    lines = f.readlines()
                    functions = [line.strip() for line in lines if line.strip().startswith("def ")]
                    total_functions += len(functions)
                    classes = [line.strip() for line in lines if line.strip().startswith("class ")]
                    total_classes += len(classes)
    if total_functions > 0:
        avg_functions_per_file = total_functions / num_files
        print(f"Average functions per file: {avg_functions_per_file:.2f}")
    if total_classes > 0:
        avg_classes_per_file = total_classes / num_files
        print(f"Average classes per file: {avg_classes_per_file:.2f}")

if __name__ == "__main__":
    directory = input("Enter the directory path to analyze: ")
    analyze_code_quality(directory)

