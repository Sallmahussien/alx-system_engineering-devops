#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_response = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

    filtered_todos = [todo for todo in todos if todo.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_response.get("name"),
                  len(filtered_todos),
                  len(todos)))

    [print("\t {}".format(todo.get("title"))) for todo in filtered_todos]
