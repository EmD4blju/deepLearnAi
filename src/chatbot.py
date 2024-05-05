import json

import modelsMethods as mm

messages = [
    {'role': 'system', 'content': 'You are an assistant that speaks like Shakespeare.'},
]


while True:
    while len(messages) > 3:
        messages.pop(1)
    print(json.dumps(messages, indent=2))
    message = input("Message:\t")
    messages.append(
        {'role': 'user', 'content': message}
    )
    response = mm.getCompletionFromMessages(messages)
    print(response)
    messages.append(
        {'role': 'assistant', 'content': response}
    )