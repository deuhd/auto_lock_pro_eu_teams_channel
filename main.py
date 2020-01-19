import discord
from discord.ext import commands
from discord.ext.commands import bot

import datetime
import asyncio

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Im ready")
    await auto_lock_unlock_main()

def get_hour_and_minute() -> list:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    seconds = datetime.datetime.now().second
    return [hour, minute, seconds]


async def auto_lock_unlock_main():
    auto = True

    while auto == True:
        now = get_hour_and_minute()
        hour = now[0]
        minute = now[1]
        seconds = now[2]
        weekday_index = datetime.datetime.today().weekday()

        cap_news_channel = client.get_channel(613372129618165761)

        team_captain_tag = "<@&627137347028254730>"
        pro_eu_team_channel_tag = "<#590184107124850688>"
        role_cap = 627137347028254730

        if hour == 0 and minute == 0 and seconds == 0 and weekday_index == 6:

            guild = ctx.guild
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True

            role_cap_get = guild.get_role(role_cap)

            await lobby_channel.set_permissions(role_cap_get, overwrite=overwrite)

            await cap_news_channel.send("Hello {},\n\n"
                                        "The {} are open!".format(team_captain_tag, pro_eu_team_channel_tag))
            auto = False

            counter = 0
            while counter < 1:
                counter += 1
                await asyncio.sleep(1)

            await auto_lock_unlock_main()

        if hour == 0 and minute == 0 and seconds == 0 and weekday_index == 0:
            guild = ctx.guild
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            overwrite.read_messages = True

            role_cap_get = guild.get_role(role_cap)

            await lobby_channel.set_permissions(role_cap_get, overwrite=overwrite)

            await cap_news_channel.send("Hello {},\n\n"
                                        "The {} now is close!".format(team_captain_tag, pro_eu_team_channel_tag))

            auto = False

            counter = 0
            while counter < 1:
                counter += 1
                await asyncio.sleep(1)

            await auto_lock_unlock_main()

client.run(token)
