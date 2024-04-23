import os
import re

def analyze_comments(file_path):
    total_lines = 0
    total_comments = 0
    single_line_comments = 0
    multi_line_comments = 0
    docstrings = 0
    todo_comments = 0
    incomplete_comments = 0
    missing_comments = 0
    consistent_conventions = True
    comment_style = None
    previous_comment = None

    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        comment_pattern = re.compile(r'#.*')
        multi_line_comment_pattern = re.compile(r'""".*?"""', re.DOTALL)

        in_multi_line_comment = False
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                continue  # Skip empty lines
            if in_multi_line_comment:
                if '"""' in line:
                    in_multi_line_comment = False
                multi_line_comments += 1
            else:
                if line.strip().startswith('"""'):
                    in_multi_line_comment = True
                    multi_line_comments += 1
                elif comment_pattern.match(line):
                    total_comments += 1
                    single_line_comments += 1
                    if 'TODO' in line:
                        todo_comments += 1
                    if 'TODO:' in line or 'TODO(' in line:
                        incomplete_comments += 1
                elif '"""' in line:
                    docstrings += 1
                else:
                    # Check if line could benefit from a comment
                    if ';' not in line and line.strip() and not line.strip().startswith("#"):
                        if previous_comment is None or line_number - previous_comment > 1:
                            missing_comments += 1
                    previous_comment = line_number

            if comment_pattern.match(line):
                # Determine comment style
                if line.strip().startswith("#"):
                    current_comment_style = "single_line"
                elif line.strip().startswith('"""'):
                    current_comment_style = "multi_line"
                else:
                    current_comment_style = None
                
                # Check consistency
                if comment_style is not None and current_comment_style != comment_style:
                    consistent_conventions = False
                comment_style = current_comment_style

    print(f"Total lines of code: {total_lines}")
    print(f"Total comments: {total_comments}")
    print(f"Total single-line comments: {single_line_comments}")
    print(f"Total multi-line comments: {multi_line_comments}")
    print(f"Total docstrings: {docstrings}")
    print(f"Total TODO comments: {todo_comments}")
    print(f"Total incomplete comments: {incomplete_comments}")
    print(f"Total missing comments: {missing_comments}")
    print(f"Consistent comment conventions: {'Yes' if consistent_conventions else 'No'}")

def analyze_files(directory):
    print("Analyzing files in directory:", directory)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print("\nFile:", file_path)
                analyze_comments(file_path)

if __name__ == "__main__":
    directory = input("Enter the directory path to analyze: ")
    analyze_files(directory)

