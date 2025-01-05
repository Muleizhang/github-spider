import requests
from bs4 import BeautifulSoup
import json
import sys

total_followers = {}
total_followings = {}

def get_followers(username, layers=1):
    url = f"https://github.com/{username}?tab=followers"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followers = []
    for follower in soup.find_all('span', class_='Link--secondary'):
        followers.append(follower.text.strip())
    total_followers[username] = followers
    print("    followers of: ", username, followers[:5] if len(followers) > 5 else followers)
    print("    total followers: ", len(followers))
    print()
    return followers

def get_followings(username, layers=1):
    url = f"https://github.com/{username}?tab=following"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followings = []
    for following in soup.find_all('span', class_='Link--secondary'):
        followings.append(following.text.strip())
    total_followings[username] = followings
    print("    followings of: ", username, followings[:5] if len(followings) > 5 else followings)
    print("    total followings: ", len(followings))
    print()
    return followings

def get_recursive_followers(username, layers):
    print("layer: ",layers)
    if layers == 0:
        return
    followers = get_followers(username, layers)
    if layers > 1:
        for follower in followers:
            get_recursive_followers(follower, layers - 1)


def get_recursive_followings(username, layers):
    print("layer: ",layers)
    if layers == 0:
        return []
    followings = get_followings(username, layers)
    if layers > 1:
        for following in followings:
            get_recursive_followings(following, layers - 1)

def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: python github_spider.py <github_username> <layers>")
        sys.exit(1)
    
    username = sys.argv[1]
    layers = int(sys.argv[2])
    followers = get_recursive_followers(username, layers)
    followings = get_recursive_followings(username, layers)
    
    data = {
        "total_followers": total_followers,
        "total_followings": total_followings
    }

    save_as_json(data, 'data.json')

if __name__ == "__main__":
    main()
