# bot.py
from twitchio.ext import commands
import telegram_send
import time

bot = commands.Bot(
    # set up the bot
    irc_token="oauth:[YOUR_TOKEN]",
    client_id="[YOUR_ID]",
    nick="[TWITCH_USER_NAME]",
    prefix="",
    initial_channels=["[CHANNEL_TO_BOT]"]
)

@bot.event
async def event_ready():
    print(f"Bot is online!")


#global variable
before = ""
count = 0
sendtime = 0

@bot.event
async def event_message(ctx):
    global before
    global count
    global sendtime

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == "[TWITCH_USER_NAME]".lower():
        return

    #We have won lol! -> #@xPapaschlumpfx has been drawn for the giveaway!
    if ctx.content.lower().startswith("@[TWITCH_USER_NAME]"):
        telegram_send.send(messages=[ctx.content])

    #update line
    if before != ctx.content:
        before = ctx.content
        #reset count
        count = 0
        return

    #lines are same
    count += 1

    #check if 95 seconds have passed since last message post
    if (time.time() - sendtime) < 95:
        return

    if count >= 15:
        #set send time
        sendtime = time.time()
        #send message
        await ctx.channel.send(before)
        f = open("log.txt", "a", encoding='utf-8')
        f.write("New Giveaway: " + ctx.content + "\n")
        f.close()


if __name__ == "__main__":
    bot.run()
