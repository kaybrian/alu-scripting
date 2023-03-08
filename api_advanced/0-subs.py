#!/usr/bin/python3
"""DOC"""
import requests


def number_of_subscribers(subreddit):
    """DOC"""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=header)

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
    return 0
