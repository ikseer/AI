import openai

openai.api_key = "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"


def chat_with_gpt(prompt):
    question = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return question.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        user_input += "\n write summary and clear answer for public people "
        if user_input.lower() in ["quit", "exit", "bye", "ciao"]:
            break

        response = chat_with_gpt(user_input)
        print("Jarvis: ", response, "\n")
