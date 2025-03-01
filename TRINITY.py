import discord
import json
import random
import ollama  # Import the Ollama package

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
    mentioned_name = next((word for word in words if word.lower() in map(str.lower, people_data.keys())), None)

    if mentioned_name:
        # Fun, chill personality mode
        role = "a chill friend who loves making jokes and having fun. Don't hesitate to make predictions about the person!. Generate response with regards to the question."
        person_info = people_data.get(mentioned_name, {})
        context = f"Here's what I know about {mentioned_name}:\n"
        context += f"- Favorite food: {person_info.get('favorite_food', 'Unknown')}\n"
        context += f"- Favorite color: {person_info.get('favorite_color', 'Unknown')}\n"
        context += f"- Hobbies: {', '.join(person_info.get('hobbies', ['Unknown']))}\n"
        context += f"- Goals: {person_info.get('goals', 'Unknown')}\n"
        context += f"- Negative aspects: {person_info.get('negative aspects', 'None')}.\n"

        bot_response = generate_response(user_input, role, context)
    else:
        # Encyclopedic assistant mode
        role = "an assistant with encyclopedic knowledge. Keep responses short and concise."
        bot_response = generate_response(user_input, role)

    await message.channel.send(bot_response)




# Run the bot with the token from environment variables
TOKEN = "MTM0MzYzODA3MjkxODY3NTQ4Nw.GVvTDt.Baa39Lew6Q0K1xhcWZJCDEzCB0yyfY1sMiG_Zk"  # Replace with your actual bot token
client.run(TOKEN)




