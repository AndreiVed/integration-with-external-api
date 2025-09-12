import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/users"
HEADERS = ("id", "name", "email")


def get_response() -> list:
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    users_data = response.json()
    data = [
        {"id": user["id"], "name": user["name"], "email": user["email"]}
        for user in users_data
    ]

    return data


def convert_to_csv(data: list) -> None:
    with open("result_data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(data)

    print("Users data just written to 'result_data.csv'")


def main() -> None:
    data = get_response()
    convert_to_csv(data)


if __name__ == "__main__":
    main()
