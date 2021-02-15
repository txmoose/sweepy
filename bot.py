import os

import discord
from discord.ext import commands

def main():
    bot = commands.Bot(command_prefix='?')

    @bot.command()
    async def sweep(ctx):
        admin = discord.utils.find(lambda r: r.name == 'Mods', ctx.guild.roles)
        print(ctx.author.roles)
        if admin not in ctx.author.roles:
            await ctx.send(f"I'm sorry ~~Dave~~ {ctx.author.name}, you're not allowed to do that.")
        else:
            try:
                print("Reading messages in channel")
                messages_to_del = await ctx.channel.history(limit=1000).flatten()
                print(f"Found {len(messages_to_del)} messages to delete")
            except discord.Forbidden:
                print("I don't have permission to read history in this channel")
                await ctx.send("I don't have permission to read history in this channel")
            except discord.HTTPException:
                print("HTTP exception on message read")
                await ctx.send("HTTP exception reading, please try again or complain to TxMoose")

            try:
                sweepy = discord.File("sweepy.jpg")
                await ctx.send("Sweeping channel", file=sweepy)
                count = 0
                for message in messages_to_del:
                    print(f"Deleting {message.id} - {count:03}")
                    count += 1
                    await message.delete()
            except discord.Forbidden:
                print("I don't have permission to delete these messages")
                await ctx.send("I don't have permission to delete these messages")
            except discord.NotFound:
                print("Message already deleted")
                await ctx.send("Message was deleted before I could do it")
            except discord.HTTPException:
                print("HTTP exception on message delete")
                await ctx.send("HTTP exception deleting, please try again or complain to TxMoose")


    bot.run(os.getenv('DISCORD_BOT_KEY'))


if __name__ == "__main__":
    main()