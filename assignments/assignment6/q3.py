import requests


def agify_demo(name):
    response = requests.get(f"https://api.agify.io/?name={name}", timeout=10)
    data = response.json()
    print("Agify API")
    print("Name:", data.get("name", "N/A"))
    print("Predicted age:", data.get("age", "N/A"))
    print("Count:", data.get("count", "N/A"))
    print()


def jsonplaceholder_demo():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    data = response.json()
    print("JSONPlaceholder API")
    print("Name:", data.get("name", "N/A"))
    print("Email:", data.get("email", "N/A"))
    print("City:", data.get("address", {}).get("city", "N/A"))
    print("Company:", data.get("company", {}).get("name", "N/A"))


agify_demo("rahul")
jsonplaceholder_demo()
