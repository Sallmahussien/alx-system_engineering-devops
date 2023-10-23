#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    username = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

    json_dict = {
        "{}".format(user_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username.get("username")
            } for todo in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as file:
        json.dump(json_dict, file)
