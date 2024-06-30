responses = []

while True:
    response = input("Why do you like programming? (or 'q' to quit): ")
    if response.lower() == 'q':
        break
    responses.append(response)

with open('programming_poll.txt', 'a') as file:
    for response in responses:
        file.write(f"{response}\n")
