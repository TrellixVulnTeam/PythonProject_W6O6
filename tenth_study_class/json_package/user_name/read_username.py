import json

filename = "username.json"
with open(filename) as obj:
    username = json.load(obj)
    print("Welcome back, " + username + "!")

