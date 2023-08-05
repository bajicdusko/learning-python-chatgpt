import httpx
import time

def fetch_github_repos(usernames, sleep_time=2):
    base_url = "https://api.github.com"
    headers = {"Accept": "application/vnd.github.v3+json"}

    for username in usernames:
        try:
            with httpx.Client() as client:
                response = client.get(f"{base_url}/users/{username}/repos", headers=headers)
                response.raise_for_status()

                repos = response.json()

                for repo in repos:
                    print(f"Repo: {repo['name']}")
                    print(f"Description: {repo['description']}")
                    print(f"Stars: {repo['stargazers_count']}")
                    print(f"Forks: {repo['forks_count']}")
                    print("\n---\n")

                # Sleep between requests to avoid hitting rate limit
                time.sleep(sleep_time)

        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred for user {username}: {http_err}")

        except Exception as err:
            print(f"An error occurred for user {username}: {err}")

# Provide list of GitHub usernames
usernames = ["bajicdusko"]
fetch_github_repos(usernames)