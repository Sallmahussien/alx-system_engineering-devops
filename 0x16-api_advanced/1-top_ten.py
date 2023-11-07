#!/usr/bin/python3
"""Implement top_ten function"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the first 10 hot posts titles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    headers = {'User-Agent': 'custom user-agent'}

    response = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return

    for post in response.json().get('data', {}).get('children', []):
        print(post.get('data', {}).get('title', ''))
