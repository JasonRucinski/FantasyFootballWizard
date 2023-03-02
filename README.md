# FantasyFootballWizard

This will be a chatbot hooking into openai chatgpt. To be used for general shit-talking between friends and I will try to update it for fantasy specific appliactions.


To run this program locally, you can follow these steps:

Install Python:
If you do not already have Python installed on your computer, download and install the latest version of Python from the official website: https://www.python.org/downloads/


Install Required Libraries:
The program requires the discord and openai libraries. You can install them using pip, which is included with Python. Open a command prompt or terminal and run the following commands:

Copy code
pip install discord
pip install openai
pip install python-dotenv


Set Up OpenAI API Key:
Make sure you have set up the OpenAI API key on your local machine, and it is correctly configured. You can follow the instructions provided by OpenAI here: https://beta.openai.com/docs/api-reference/authentication


Create a Discord Bot:
If you haven't already, create a new Discord bot by following the instructions provided by Discord: https://discordpy.readthedocs.io/en/stable/discord.html


Add the Bot Token:
Once you have created a Discord bot, add its token to the client.run() method in the code. Replace <your Discord bot token> with the actual token of your Discord bot.


Run the Program:
Save the modified code to a file, e.g. discord_bot.py, and run it from the command prompt or terminal by navigating to the directory where the file is located and running the command:

Copy code
python discord_bot.py
The program will start running and will be listening for incoming messages on the Discord channel associated with the bot. You can test the program by sending a message to the channel and seeing if the bot responds.
