import discord
import responses

async def send_message(message, user_message,channel):
    try:
        response = responses.get_response(user_message)
        if channel == 'general':
            await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTAzOTQ2MzY3NDc4NTU3MDgxNg.GJ66Qc.u7uXotzMYj3boCURRiuH5JKiQPNUf-wicXG180'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_message = str(message.content)
        channel = str(message.channel)

        await send_message(message, user_message, channel)
    client.run(TOKEN)
