import openai

openai.api_key = "OPENAI_API_KEY"

while True:
    user_prompt = input("Enter your prompt or press q to quit: ")
    if user_prompt == "q":
        break
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": user_prompt}
    ],
    max_tokens=100)

    print("Total tokens:", response.usage.total_tokens)
    print(response.choices[0].message.content)
