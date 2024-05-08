import openai

def chat_with_gpt(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    api_key = 'your-api-key-here'  # Replace with your actual OpenAI API key
    user_input = input("You: ")
    response = chat_with_gpt(user_input, api_key)
    print("GPT-4:", response)
