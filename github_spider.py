import requests
from bs4 import BeautifulSoup
import json
import sys

def get_followers(username):
    url = f"https://github.com/{username}?tab=followers"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followers = []
    for follower in soup.find_all('span', class_='Link--secondary'):
        followers.append(follower.text.strip())
    return followers

def get_followings(username):
    url = f"https://github.com/{username}?tab=following"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followings = []
    for following in soup.find_all('span', class_='Link--secondary'):
        followings.append(following.text.strip())
    return followings

def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python github_spider.py <github_username>")
        sys.exit(1)
    
    username = sys.argv[1]
    followers = get_followers(username)
    followings = get_followings(username)
    
    save_as_json(followers, 'followers.json')
    save_as_json(followings, 'followings.json')

if __name__ == "__main__":
    main()
