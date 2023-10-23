#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    username = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

    csv_list = [
        {
            "USER_ID": user_id,
            "USERNAME": username.get("username"),
            "TASK_COMPLETED_STATUS": todo.get("completed"),
            "TASK_TITLE": todo.get("title")
        }
        for todo in todos
    ]

    with open("{}.csv".format(user_id), 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=csv_list[0].keys(),
                                quoting=csv.QUOTE_ALL
                                )

        writer.writerows(csv_list)
