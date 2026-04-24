import json
import requests

def load_tests():
    with open("data/generated_tests.json", "r") as f:
        return json.load(f)

def test_api_cases():
    test_cases = load_tests()

    assert len(test_cases) > 0

    for test in test_cases:
        response = requests.get(test["endpoint"])
        assert response.status_code == test["expected_status"]