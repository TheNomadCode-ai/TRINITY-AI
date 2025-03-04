# Discord Chatbot - Your Fun Mutual Friend

## Overview
This is a locally hosted AI chatbot designed for a Discord server. It acts as a fun mutual friend by remembering users, referencing a JSON database for personalized responses, and engaging in natural conversations. Unlike cloud-based bots, this one runs entirely on your system, ensuring privacy and no API token limits.

## Features
- **Personalized Responses**: The bot references a JSON file containing user details such as interests and hobbies.
- **Memory & Context Awareness**: It remembers previous interactions to make conversations more natural.
- **Friend-Like Behavior**: If asked about a friend, it checks the JSON and responds logically or humorously.
- **Locally Hosted**: No external API calls, making it faster and more reliable.
- **General Chatbot Abilities**: Can handle normal chatbot conversations beyond referencing JSON data.

## Requirements
Ensure you have the following installed before running the bot:
- Python 3.8+
- Discord.py (`pip install discord`)
- OpenAI API (if using an AI model, install `pip install openai`)
- JSON support (`pip install orjson` for faster parsing, or built-in `json` module)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/discord-chatbot.git
   cd discord-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `config.json` file:
   ```json
   {
     "token": "YOUR_DISCORD_BOT_TOKEN",
     "prefix": "!",
     "json_file": "data/users.json"
   }
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage
- Mention the bot or use the prefix to interact.
- Ask it about a friend in the server, and it will respond based on the JSON data.
- Chat normally, and the bot will remember details over time.

## Customization
- **Modify `data/users.json`** to add or update user details.
- **Adjust `bot.py`** to tweak response behavior or add commands.

## Future Upgrades
- Implement a memory search feature.
- Add AI-generated responses with personality.
- Allow users to contribute to the bot's memory dynamically.

## Contributing
Feel free to fork the project and submit pull requests with improvements!

## License
MIT License. Free to use and modify.


