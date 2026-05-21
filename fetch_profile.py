import requests

def get_profile(username):
    
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    data = response.json()
    
    return {
        "name": data.get("name"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "public_repos": data.get("public_repos")
    }


if __name__ == "__main__":
    
    username = input("GitHub Username: ")
    
    profile = get_profile(username)
    
    print(profile)