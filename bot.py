import discord

import releasedate
import responses
import os


async def send_message(message, user_message, channel):
    try:
        response = responses.get_response(channel, user_message)
        date = releasedate.get_release_date()
        if channel == 'general':
            await message.channel.send(response)
            if len(response) > 0:
                await message.channel.send(date)
    except Exception as e:
        print(e)


def run_discord_bot():
    token = 'MTAzOTQ2MzY3NDc4NTU3MDgxNg.G0egCd.mbUeA52EbpKVWJYFvSvoIGiTCaa0190ie974gs'
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
    client.run(token)
