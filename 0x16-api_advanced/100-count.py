#!/usr/bin/python3
"""Implement count_words function"""

import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
        queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'custom user-agent'}

    response = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print()
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
