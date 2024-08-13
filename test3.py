import openai
# Initialize the OpenAI client
openai.api_key = 'sk-proj-rDyiyv34crnOdY4h5cBjT3BlbkFJrsgJwrsX6MVJLNV0pluw'
# Create a completion
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hi how are you?"}
  ]
)

# Extract and print the results
print("Message: ", completion.choices[0].message['content'])
print("Usage: ", completion.usage)
print("Prompt tokens: ", completion.usage['prompt_tokens'])
print("Completion tokens: ", completion.usage['completion_tokens'])
print("Total tokens: ", completion.usage['total_tokens'])
