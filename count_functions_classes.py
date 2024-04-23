import os
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_functions(filepath):
    functions = {}

    with open(filepath, "r") as file:
        tree = ast.parse(file.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name
                function_code = ast.unparse(node)
                functions[function_name] = function_code

    return functions

def train_model(training_data):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(training_data.values())
    return features

def evaluate_similarity(features, function_code):
    vectorizer = TfidfVectorizer()
    function_features = vectorizer.transform([function_code])
    similarity = cosine_similarity(features, function_features)
    return similarity.max()  # Assuming binary classification (similar vs. dissimilar)

def analyze_modularity(directory):
    training_data = {}  # Dictionary to store labeled training data
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                functions = extract_functions(filepath)
                for function_name, function_code in functions.items():
                    # Assign a label to each function based on its behavior
                    # Example: training_data[function_name] = behavior_label
                    training_data[function_name] = behavior_label

    features = train_model(training_data)
    similarity_threshold = 0.8  # Adjust as needed
    similar_functions = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                functions = extract_functions(filepath)
                for function_name, function_code in functions.items():
                    similarity = evaluate_similarity(features, function_code)
                    if similarity > similarity_threshold:
                        similar_functions.append((file, function_name))

    print("Similar functions:")
    for file, function_name in similar_functions:
        print(f"In file {file}: Function {function_name}")

if __name__ == "__main__":
    directory = input("Enter the directory path to analyze: ")
    analyze_modularity(directory)

