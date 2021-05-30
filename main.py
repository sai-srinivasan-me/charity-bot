import discord
from discord import asset
from discord.ext import commands
from random import randint
import json
import asyncio

command_prefix = 'ct.'

client = commands.Bot(command_prefix='lkasdhlashdkjashdkajhsdk')

blklistwords = open("blacklistedwords.txt", "r")
blacklistedwords = blklistwords.read()
blacklist_words = blacklistedwords.split(",")
blklistwords.close()



@client.event
async def on_ready():
    print('Servers connected to:')
    for guild in client.guilds:
        print(str(guild.name))

@client.event
async def on_member_join(member):
    print(f'New Member! {member}')

"""
@client.command()
async def configembed(ctx):
    global sconfig
    desc = f'''
Server Default Role: {sconfig["server_default_role_id"]}
    '''
    configembed = discord.Embed(
        title='⚙️ Server Config ⚙️',
        description=desc,
        color=0xFAE700
    )
    await ctx.send(embed=configembed)
"""

@client.event
async def on_message(ctx):
    # Call Server Config JSON
    json_file = open("sconfig.json")
    sconfig = json.load(json_file)
    json_file.close()
    # Moderation Filter
    message_string = ctx.content
    global blacklist_words
    for word in blacklist_words:
        if word in message_string:
            user = ctx.author
            user_DM = await user.create_dm()
            await ctx.delete()
            warn_id = randint(10000, 100000000000)
            desc = f'''
__**VIOLATION DETAILS**__
Message: `{ctx.content}`
Blacklisted Content: `{word}`
Violation ID: `{warn_id}`
Action: `MUTE`

__Want to appeal or have a question?__
Please DM our support team.
            '''
            embed_dm = discord.Embed(
                title='You have recieved a violation.',
                description=desc,
                color=0x80d4ff
            )
            await user_DM.send(embed=embed_dm)
    # Checking if its a command
    splitted_msg = list(ctx.content)
    print(splitted_msg)
    print(''.join(splitted_msg[:3]))
    if ''.join(splitted_msg[:3]) == 'kp.':
        try:
            if ''.join(splitted_msg[3:17]) == 'changemainrole':
                role_splitted = []
                for x in splitted_msg[18:]:
                    print(x)
                    if x == '>':
                        role_splitted.append(x)
                        role = ''.join(role_splitted)
                        print(role_splitted)
                        break
                    else:
                        role_splitted.append(x)
                with open("sconfig.json", "r") as jsonFile:
                    data = json.load(jsonFile)

                data["server_default_role_id"] = role

                with open("sconfig.json", "w") as jsonFile:
                    json.dump(data, jsonFile)

                json_file = open("sconfig.json")
                sconfig = json.load(json_file)
                json_file.close()
                return
            if ''.join(splitted_msg[3:17]) == 'changecslechan':
                channel_splitted = []
                for x in splitted_msg[18:]:
                    print(x)
                    if x == '>':
                        channel = ''.join(channel_splitted)
                        print(channel_splitted)
                        break
                    elif x == '@':
                        pass
                    elif x == '#':
                        pass
                    elif x == '<':
                        pass
                    else:
                        channel_splitted.append(x)
                with open("sconfig.json", "r") as jsonFile:
                    data = json.load(jsonFile)

                data["discord_console"] = channel

                with open("sconfig.json", "w") as jsonFile:
                    json.dump(data, jsonFile)

                json_file = open("sconfig.json")
                sconfig = json.load(json_file)
                json_file.close()
                return
            if ''.join(splitted_msg[3:15]) == 'configembed':
                desc = f'''
Server Default Role: {sconfig["server_default_role_id"]}
Discord Channel Console: <#{sconfig["discord_console"]}>
                '''
                configembed = discord.Embed(
                    title='⚙️ Server Config ⚙️',
                    description=desc,
                    color=0xFAE700
                )
                await ctx.channel.send(embed=configembed)
                return
            if ''.join(splitted_msg[3:8]) == 'purge':
                try:
                    amt = int(''.join(splitted_msg[9:]))
                    messages = []
                    async for message in ctx.channel.history(limit=int(amt) + 1):
                        messages.append(message)
                    await ctx.channel.delete_messages(messages)
                except ValueError as e:
                    notifymsg = await ctx.channel.send('You can only purge a __number__ or messages, not text.')
                    print(e)
                    console_channel = client.get_channel(848382773478555689)
                    printmsg = f'__Message Redirect:__\n[Click Here!](https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id})\n\n__Error Output__\n```{e}```'
                    error_embed = discord.Embed(
                        title='ERROR',
                        description=printmsg,
                        color=0xFF5733
                    )
                    await console_channel.send(embed=error_embed)
                    await asyncio.sleep(2)
                    await notifymsg.delete()
                    return



            
        except Exception as e:
            print(e)
            console_channel = client.get_channel(848382773478555689)
            printmsg = f'__Message Redirect:__\n[Click Here!](https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.id})\n\n__Error Output__\n```{e}```'
            error_embed = discord.Embed(
                title='ERROR',
                description=printmsg,
                color=0xFF5733
            )
            await console_channel.send(embed=error_embed)
            return

        
    
'''
@client.command()
async def changemainrole(ctx, role: discord.Role):
    with open("sconfig.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["server_default_role_id"] = role

    with open("sconfig.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    json_file = open("sconfig.json")
    global sconfig
    sconfig = json.load(json_file)
    json_file.close()


@client.command()
async def test(ctx):
    print(ctx.channel.id)
'''
client.run('ODQ4MDI4MzM4Njk4NDUzMDEy.YLGp7w.tMeBX1K_GB5yAszMGR9frHU0FeE')
