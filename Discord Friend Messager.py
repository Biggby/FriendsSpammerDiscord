import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
       await user.send("""Message""")
       print(f"messaged: {user.name} But they're a bitch")
    except:
       print(f"couldnt message: {user.name} Blocked whore")

client.run('token', bot=False)
