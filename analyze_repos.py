import requests

def get_languages(username):
    
    repos_url = f"https://api.github.com/users/{username}/repos"
    
    repos = requests.get(repos_url).json()
    
    language_count = {}
    
    for repo in repos:
        
        language = repo.get("language")
        
        if language:
            
            language_count[language] = (
                language_count.get(language, 0) + 1
            )
    
    return language_count


if __name__ == "__main__":
    
    username = input("GitHub Username: ")
    
    print(get_languages(username))