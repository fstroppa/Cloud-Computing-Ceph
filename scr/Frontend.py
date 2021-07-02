import os

while not exit:
    prompt = input("> ")
    splits = prompt.split()
    if len((splits)) < 1:
        continue

    command = splits[0]

    if command == "!test":
        print("send to server")
        os.system("http://252.3.233.130:8080/")

