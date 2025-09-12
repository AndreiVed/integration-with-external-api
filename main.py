import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/users"
HEADERS = ("id", "name", "email")


def get_response() -> list | None:
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        users_data = response.json()
        if not isinstance(users_data, list):
            raise ValueError("Data is not a list")

        return [
            {"id": user["id"], "name": user["name"], "email": user["email"]}
            for user in users_data
        ]

    except Exception as e:
        print(f"An unexpected error occurred: {e} ")

    return None


def convert_to_csv(data: list) -> None:
    try:
        with open("result_data.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(data)
        print("Users data just written to 'result_data.csv'")
    except IOError as e:
        print(f"An unexpected error while writing data to file: {e} ")
        raise


def main() -> None:
    try:
        data = get_response()
        if data:
            convert_to_csv(data)
    except Exception as e:
        print(f"Operation ended with error: {e}")


if __name__ == "__main__":
    main()
