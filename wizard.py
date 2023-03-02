import discord
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Discord client
client = discord.Client()

# Set up the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define a function to generate responses using GPT-3
def generate_response(prompt):
    # Set up the GPT-3 parameters
    model_engine = "davinci" # Or any other GPT-3 engine you have access to
    prompt = f"{prompt}\nAI:"

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()

    return response_text

# Define a function to handle Discord messages
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Generate a response using GPT-3
    prompt = message.content
    response = generate_response(prompt)

    # Send the response back to the same channel
    await message.channel.send(response)

# Run the Discord client
client.run(os.environ.get("DISCORD_TOKEN"))