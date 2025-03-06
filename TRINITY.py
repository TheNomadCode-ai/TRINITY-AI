import discord
import json
import ollama  # Import the Ollama package
import os


# Define the path to the JSON file
JSON_PATH = "peoples_data.json"  # Ensure this file is uploaded to Replit in the root directory


# Load JSON data from the file
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Function to generate a response using Ollama
def generate_response(user_input, role, context=""):
    try:
        messages = [
            {"role": "system", "content": f"You are TRINITY, {role}"},
            {"role": "user", "content": context + "\n\n" + user_input if context else user_input}
        ]

        response = ollama.chat(model="llama2", messages=messages)
        bot_response = response['message'][
            'content'] if 'message' in response else "Sorry, I couldn't generate a response."
        return bot_response[:1997] + "..." if len(bot_response) > 2000 else bot_response  # Truncate if too long

    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."


# Load the JSON data
people_data = load_json(JSON_PATH)

# Discord bot client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore bot's own messages

    user_input = message.content.strip()

    # Ensure the input starts with "TRINITY,"
    if not user_input.startswith("TRINITY,"):
        return  # Exit the function if input doesn't start with "TRINITY,"

    words = user_input.split()
    mentioned_name = next(
        (word for word in words if any(name.lower().startswith(word.lower()) for name in people_data.keys())), None)

    if mentioned_name:
        # Find the full name from the JSON data
        full_name = next(name for name in people_data.keys() if name.lower().startswith(mentioned_name.lower()))

        # Fun, chill personality mode
        role = "a chill friend who loves making jokes and having fun. Generate response with regards to the question and the context about the person while being lighthearted"
        person_info = people_data.get(full_name, {})
        context = f"Here's what I know about {full_name}:\n"
        context += f"- {person_info.get('description', '')}\n"
        context += f"- Favorite food: {person_info.get('favorite_food', 'Unknown')}\n"
        context += f"- Favorite color: {person_info.get('favorite_color', 'Unknown')}\n"
        context += f"- Hobbies: {', '.join(person_info.get('hobbies', ['Unknown']))}\n"
        context += f"- Goals: {person_info.get('goals', 'Unknown')}\n"
        context += f"- Negative aspects: {person_info.get('negative aspects', 'None')}."

        bot_response = generate_response(user_input, role, context)
    else:
        # Encyclopedic assistant mode
        role = "an assistant with encyclopedic knowledge. Keep responses short and concise."
        bot_response = generate_response(user_input, role)

    await message.channel.send(bot_response)


load_dotenv()  # Load environment variables from .env file

TOKEN = os.environ["BOT_TOKEN"] # Get the bot token from environment variables
client.run(TOKEN)




