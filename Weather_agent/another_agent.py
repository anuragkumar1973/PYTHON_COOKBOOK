from anthropic import AnthropicFoundry

endpoint = "https://anuragkumar1973-0503-resource.openai.azure.com/anthropic"
deployment_name = "claude-opus-4-7"
api_key = "YOUR_API_KEY_HERE"

client = AnthropicFoundry(
    api_key=api_key,
    base_url=endpoint
)

message = client.messages.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "How is the weather in Seattle today?  "}
    ],
    max_tokens=1024,
)

print(message.content)