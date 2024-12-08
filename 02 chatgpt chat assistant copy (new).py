import openai

openai.api_key = "APIkeys"

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    message = input("YOU: ")

    if message.lower() == "quit()":
        print("Goodbye!")
        break
    
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})

    print("\nCHATBOT: " + reply + "\n")
