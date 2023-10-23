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

    users = requests.get("{}users".format(url)).json()
    todos = requests.get("{}todos".format(url)).json()

    json_dict = {
        "{}".format(user.get("id")): [
            {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            } for todo in todos if todo.get("userId") == user.get("id")
        ] for user in users
    }

    with open("todo_all_employees.json", "w") as file:
        json.dump(json_dict, file)
