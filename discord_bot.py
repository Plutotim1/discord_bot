import discord

class MyClient(discord.Client):

    #log-in
    async def on_ready(self):
        print("eingelogt")
    
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith("hallo"):
            await message.channel.send(f"Hallo, {message.author}!")

    async def on_message_delete(self, message):
        if message.author != client.user:
            await message.channel.send(f"{message.author} deleted: {message.content}")
    
    async def on_message_edit(self, before, after):
        print("a")
        if before.content != after.content:
            await after.channel.send(f"{before.author} edited his message from '{str(before.content)}' to '{str(after.content)}'")

client = MyClient()
client.run("ODY5NjE4MjE3NTcwNjgwODYz.YQA1Ew.r3UnttxVcaogEzXp_rqRc0SyxKE")
