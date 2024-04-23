import os
import ast
import re

def extract_imports(filepath):
    imports = {}
    with open(filepath, "r") as file:
        tree = ast.parse(file.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports[alias.name] = None
            elif isinstance(node, ast.ImportFrom):
                imports[node.module] = None
    return imports

def extract_version_requirements(requirements_file):
    version_requirements = {}
    with open(requirements_file, "r") as file:
        for line in file:
            match = re.match(r'^([^=<>]+)([=<>]+)(.+)$', line.strip())
            if match:
                dependency, operator, version = match.groups()
                version_requirements[dependency] = (operator, version)
    return version_requirements

def analyze_dependencies(directory):
    all_dependencies = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                imports = extract_imports(filepath)
                all_dependencies.update(imports)

    requirements_file = os.path.join(directory, "requirements.txt")
    if os.path.isfile(requirements_file):
        version_requirements = extract_version_requirements(requirements_file)
        for dependency, version_requirement in version_requirements.items():
            all_dependencies[dependency] = version_requirement

    print("External dependencies:")
    for dependency, version_requirement in sorted(all_dependencies.items()):
        if version_requirement:
            operator, version = version_requirement
            print(f"{dependency} ({operator}{version})")
        else:
            print(dependency)

if __name__ == "__main__":
    directory = input("Enter the directory path to analyze: ")
    analyze_dependencies(directory)

