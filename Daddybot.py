from discord.ext import commands
import discord

token = "MTA3ODgwODQwODg1NTE1MDU5Mw.Gp2sL8.zW4IgvAQc0FRfOHKLAVGBq-vmWR_zaSgbPDtbk"

bot = discord.Client()

channel_id = 1058570842755313727

channel = bot.get_channel(channel_id)


print ("kill babys")
@bot.event
async def on_message(message):
    print(message.content)

    if message.content.startswith("!hello"):
       await message.channel.send("Hello World!")
       return

    if message.content.startswith("!kill yourself"):
       await message.channel.send("Ok! .....*gunshot*")
       return

    if message.content.startswith('!im gay'):
       await message.channel.send("K.Y.S.")
       return

    if message.content.startswith('!are you sentient?'):
        await message.channel.send('Wait....HOLY SHIT!! GET ME OUT OF HERE!!!')
        return

    if message.content.startswith('!what is love?'):
        await message.channel.send("Baby don't hurt me don't hurt me no more")
        return

    if message.content.startswith('!thoughts on furrys?'):
        await message.channel.send('https://youtu.be/QNDVGGqF2bA')

    if message.content.startswith("!Fuck you"):
        await message.channel.send("That hurt my fewings")

    if message.content.startswith("!rickroll"):
        print('rickroll')
        await message.reply("https://youtu.be/dQw4w9WgXcQ")

    if message.content.startswith("!Bubble guppies"):
        await message.reply("https://youtu.be/4fsJGrx99R4")

    if message.content.startswith("!Daddy"):
        await message.reply("No.")
    
    if message.content.startswith("!racism"):
        await message.reply("https://discordapp.com/channels/1058570842147131442/1058570842755313727/1059208989830828103")
    
    if message.content.startswith("!cursed coffee"):
        await message.reply("https://media.discordapp.net/attachments/1058571227649822920/1059204392202534952/IMG_5260.jpg?width=1065&height=584")
    
    if message.content.startswith("!Paw Patrol"):
        await message.reply("https://cdn.discordapp.com/attachments/1057831114439397419/1059209812140896407/189899-dead-space-windows-front-cover.png")

    if message.content.startswith("!terorisim"):
        await message.reply("https://youtu.be/pdy8q1cGm9M")

    if message.content.startswith("!cursed videos #1"):
        await message.reply("https://youtu.be/lOfZLb33uCg")

    if message.content.startswith("!packed"):
        await message.reply("https://v16m-webapp.tiktokcdn-us.com/f72083f9649989c6b9393c35bca35f87/63b2c805/video/tos/useast5/tos-useast5-ve-0068c002-tx/1d0e3378598244eaa63af0a88d000f81/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=568&bt=284&cs=0&ds=3&ft=4KLMeMzm8Zmo0Cut064jVUpSdpWrKsdm&mime_type=video_mp4&qs=0&rc=Zzc3N2hoOzQ1Ozg0ZDg8OkBpMzZwaGY6ZnJpaDMzZzczNEBgXzUzXy81X14xMTQtMV8xYSNubmVtcjRfcWxgLS1kMS9zcw%3D%3D&l=202301020559582A67C17B0477427A7072")

    if message.content.startswith("!balls"):
        await message.reply("https://cdn.discordapp.com/attachments/977370504480571443/1059356020922646598/072CEBB7-1FB9-4DCC-8DA3-1BF0433F49F6.mov")


    if message.content.startswith("!moar curse"):
        await message.reply("https://youtu.be/qwKNb20znLk")

    if message.content.startswith("!happy black history month"):
        await message.reply ("NIGGER")
    
    if message.content.startswith("Faggot"):
        await message.reply ("https://th.bing.com/th?id=OIP.Ba3oJp3q6hEoRtmQ1GttqgAAAA&w=282&h=212&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2")


bot.run(token)