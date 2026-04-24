import json
import os

# asegurar que exista la carpeta data
os.makedirs("data", exist_ok=True)

def generate_test_cases():
    test_cases = [
        {
            "name": "Valid GET posts",
            "endpoint": "https://jsonplaceholder.typicode.com/posts",
            "expected_status": 200
        },
        {
            "name": "Invalid endpoint",
            "endpoint": "https://jsonplaceholder.typicode.com/invalid",
            "expected_status": 404
        }
    ]

    with open("data/generated_tests.json", "w") as f:
        json.dump(test_cases, f, indent=4)

    print("Test cases generados correctamente")

if __name__ == "__main__":
    generate_test_cases()