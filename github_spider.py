import requests
from bs4 import BeautifulSoup
import json
import sys

def get_followers(username, layers=1):
    url = f"https://github.com/{username}?tab=followers"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followers = []
    for follower in soup.find_all('span', class_='Link--secondary'):
        followers.append(follower.text.strip())
    return followers

def get_followings(username, layers=1):
    url = f"https://github.com/{username}?tab=following"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    followings = []
    for following in soup.find_all('span', class_='Link--secondary'):
        followings.append(following.text.strip())
    return followings

def get_recursive_followers(username, layers):
    if layers == 0:
        return []
    followers = get_followers(username)
    all_followers = followers[:]
    for follower in followers:
        all_followers.extend(get_recursive_followers(follower, layers - 1))
    return all_followers

def get_recursive_followings(username, layers):
    if layers == 0:
        return []
    followings = get_followings(username)
    all_followings = followings[:]
    for following in followings:
        all_followings.extend(get_recursive_followings(following, layers - 1))
    return all_followings

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
    
    save_as_json(followers, 'followers.json')
    save_as_json(followings, 'followings.json')

if __name__ == "__main__":
    main()
