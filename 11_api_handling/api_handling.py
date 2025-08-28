import requests

BASE_URL = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_random_user():
    response = requests.get(BASE_URL)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch random user")


def main():
    try:
        username, country = fetch_random_user()
        print(f"username: {username}, country: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
