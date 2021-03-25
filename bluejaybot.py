import discord
import time
import random
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

#import the discord package


#Client (this is our bot stored in the variable client)
client = commands.Bot(command_prefix="+")
client.remove_command('help')
status = cycle(['Soaring through the air! |+help','Made by 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432! |+help ','+help for help!', 'Help + Support: https://discord.gg/SQfteTVKnY'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot online!')
    
   

@tasks.loop(seconds=10) 
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))


@client.event
async def on_disconnect():
    print('Bot offline')
    await client.change_presence(status=discord.Status.invisible)
    



@client.event
async def on_member_join(member):
    if member.guild.name == 'Gamer House': 
        embed = discord.Embed(title=f'welcome {member.mention} !\nWelcome to {member.guild.name} go see #reaction-roles and #rules! ',
                    color=0x0061ff,
                    font_size=200)
        await client.get_channel(805851297696972852).send(f"{member.mention} just joined the flight!")
        await client.get_channel(818537693465018429).send(f'Hi, {member.mention}! Welcome to {member.guild.name}! TYpe +verify to verify yourself!')
        role = discord.utils.get(member.guild.roles, name="Unverified")
        await member.add_roles(role)
        await member.send(f'**Welcome to the Gamer House!**\nHey, {member.mention}, welcome to the Gamer Hosue! We hope you read the #rules so you don\'t get *detention* and you go to #reaction-roles to get some roles so you don\'t get misidentified or missed out on some HEISTS, EVENTS, GIVEAWAYS, AND MORE! **YOU ARE PROBABLY WONDERING: WAIT, WHERE\'S THE REST OF THE SERVER?? WELL, TO GAIN ACCESS TO IT, JUST JTYPE "+verify"! ')

    else:
        embed = discord.Embed(title=f'Wazzup, welcome to {member.guild.name}!', value=f'Hey, {member.mention}, welcome to {member.guild.name}! Type +rules to see the rules of the server and thn prepare yourself for some FUN! Hope you have a blast here!\nBy the way, check out my original server: the Gamer House! I was coded by 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 so if anything goes wrong, contact him! Here\'s the link: https://discord.gg/tfBZ7FZejn')
        await member.send(embed=embed)
    














#help ------------------------------------------------------------------------------------------

@client.command(name='help')
async def help(context):
    helpEmbed = discord.Embed(title='Help is here!', description='Here are all of the different types of commands! Type +help [command type] for a specific category!', color=0x00FF00)
    helpEmbed.add_field(name='Useful Commands: ', value='**+help**\ndms you the help page\n\n**+report [user] [reason]**\nreports a user for breaking a rule\n\n**+verify**\nverifies yourself to become a member\n\n**+rules**\nDMs the rules of the server\n\n**+dm [user] [message]**\nDMs a message to a user\n\n**+send [message]**\nsends a message') 
    helpEmbed.add_field(name='Commands for moderators with admin perms:', value='**+kick [user][reason]\n +ban [user][reason]**\nanybody with a head would know what these commands do\n\n**+warn [user][reason]**\nwarns a user for something\n\n**+confirm [user][message ID]**\nconfirms a verification\n\n**+close [message id][reason]**\ncloses a reported case\n\n**+override [user] [message_id]**\noverrides a verification process')
    helpEmbed.add_field(name='Fun Commands:', value='**+guilds**\nshows how many guilds (servers) this bot is in\n\n**+rickroll**\ngenerates a rickroll link\n\n**+spam [user][message]**\nspams a message 50 times to a user (DMs it)')
    helpEmbed.add_field(name='Game Commands: ', value='**ROCK PAPER SCISSORS**\n+rock, +paper, +scissors\nenters these moves to start a game')
    helpEmbed.set_author(name='Flying Helper')
    helpEmbed.add_field(name='Invite me to your servers!', value='The Blue Jay Bot is expanding itself, so it would be REALLY helpful if you invited me! Once the invitation is confirmed, you will become a **CONTRIBUTOR** for the bot! That includes exptra perks like hidden commands (yes there are some) and to use some commands without the permissions required! Just type **+invite**!')
    helpEmbed.set_footer(text='Version 3.23.2021')
    await context.message.channel.send('Sent you a DM with the help page!')
    await context.message.author.send(embed=helpEmbed)








#help ------------------------------------------------------------------------------------------


















@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        embed1 = discord.Embed(title='Sorry, looks like you cannot use that command!',description='Sorry, this command is only for moderators. You do not have permission to use that command.', color=0xFF0000)
        await ctx.send(embed=embed1)
    if isinstance(error, commands.CommandNotFound):
        embed2 = discord.Embed(title='Whoops, that\'s not a command!', description='The command you just entered was not found. Check the help page (+help) and check your message. If you think that was an error, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        await ctx.send(embed=embed2)        





#Hidden 


@client.command(name='test')
@commands.has_permissions(administrator=True)
async def test(context):
    await context.message.author.send('Bot online!')
    embed2 = discord.Embed(title='Whoops, that\'s not a command!', description='The command you just entered was not found. Check the help page (+help) and check your message. If you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
    await context.message.channel.send(embed=embed2)
    









































#Useful Commands

@client.command(name='report', pass_content=True)
async def report(context, member: discord.Member, *, reason=None):
    try:
        reason = reason
        user = context.message.author.name
        wEmbed = discord.Embed(title='Reported user!', description=f'**Report Stats**\nUser reported: {member.mention}\nReason for report: '+reason+'\nReported by: '+str(user), color=0xFF0000)
        await context.message.channel.send(embed=wEmbed)
        await context.message.channel.send('<@&815308385875394560>')
    except:
        e = discord.Embed(title='Error: Something Unexpected Happened!', description='Failed to execute command! The correct usage for this command is +report [mention user] [reason]\n**Examples:**\n+report @wazzup#4253 cussing\n+report @supaclan#9688 spamming mentions\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        await context.message.channel.send(embed=e)


    
@client.command(name='verify')
async def verify(context):
    veEmbed = discord.Embed(title='Verifier', description='You will need to verify in order to gain access to the server', color=0x00FF00)
    veEmbed.add_field(name='Verification Questions', value='Please answer these questions truthfully:\n1. How did you find this server?\n2. Have you read the rules?\n3. What are rules #2 and #4?\n4. Do you wish to have fun?')
    veEmbed.set_author(name='Verifying...')
    veEmbed.set_footer(text='Ping @Moderators if you don\'t get verified in 15 minutes!')
    await context.message.channel.send(embed=veEmbed)




@client.command(name='rules')
async def rules(context):
    await context.message.author.send('''**Discord Server Rules:**\n1. Be respectful
You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.
2. No Inappropriate Language
The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.
3. No spamming
Don't send a lot of small messages right after each other. Do not disrupt chat by spamming.
4. No pornographic/adult/other NSFW material
This is a community server and not meant to share this kind of material.
5. No random advertisements
Please do not post any links/advertisements in any channels OTHER THAN #self-promote 
6. No offensive names and profile pictures
You will be asked to change your name or picture if the staff deems them inappropriate.
7. Server Raiding
Raiding or mentions of raiding are not allowed.
8. Direct & Indirect Threats
Threats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed.
9. Follow the Discord Community Guidelines
You can find them here: https://discordapp.com/guidelines
10. This is the MOST IMPORTANT RULE IN THIS SERVER
HAVE FUN!!!!
The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated ping the Mods and we will resolve the issue.
All Channels will have pinned messages explaining what they are there for and how everything works. If you don't understand something, feel free to ask!
Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them.
**If someone is not following the rules, please send a DM to the ModMail Bot, and the staff will review the case. **
Or, you can ping the @Report to report someone for breaking the rules.
Thank you for helping us keep our community safe!''')
    


@client.command(name='dm')
async def dm(context, member: discord.Member, *, message):
    try:
        dmEmbed = discord.Embed(title='New message!', color=0x388E8E)
        dmEmbed.set_author(name='Pigeon Friend Messenger')
        dmEmbed.add_field(name='You have a new message!', value=f'*{message}*')
        await member.send(embed=dmEmbed)
        dm1Embed = discord.Embed(title='Message Sent', color=0x00FFFF)
        dm1Embed.add_field(name=f'Sent this message to '+member.display_name+':', value=f'{message}')
        await context.message.author.send(embed=dm1Embed)
    except:
        e = discord.Embed(title='Error: Something Unexpected Happened!', description='Failed to execute command! The correct usage for this command is +dm [mention user] [message]\n**Examples:**\n+dm @wazzup#4253 hey wanna call?\n+dm @supaclan#9688 hi\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        e.set_footer(text='If that doesn\'t work, then the speicified user probably have blocked me, so I cannot DM them.')
        await context.message.channel.send(embed=e)


@client.command(name='send', pass_content=True)
async def send(context, *, message):
    await context.message.channel.send(message)


























@client.command(name='invite')
async def invite(context):
    inEmbed = discord.Embed(title='Invite me to your servers too!', description='Wanna add some flight to lift up your server? Then invite the Blue Jay Bot! Sinply click on the link below! **NOTE: You must have the manage server permissions to invite bots!**', color=0xFF00FF)
    inEmbed.add_field(name='**Blue Jay Bot Invite Link**', value='https://discord.com/api/oauth2/authorize?client_id=813499887365914624&permissions=8&scope=bot')
    await context.message.channel.send(embed=inEmbed)









#Commands for moderators

@client.command(name='kick', pass_content = True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member, *, reason=None):
    try: 
        await member.kick(reason=reason)
        await context.send('User '+member.display_name+' has been kicked for '+str(reason))
    except:
        e = discord.Embed(title='Error: Something Unexpected Happened!', description='Failed to execute command! The correct usage for this command is +kick [mention user] [reason]\n**Examples:**\n+kick @wazzup#4253 underage!!!\n+kick @supaclan#9688 breaking rules and not stopping\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        e.set_footer(text='If that does\'t work, then there must be an error - you cannot kick me or the owners!')
        await context.message.channel.send(embed=e)
    

@client.command(name='ban', pass_content=True)
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await context.send('User '+member.display_name+' has been banned for '+str(reason))
        
    except:
        e = discord.Embed(title='Error: Something Unexpected Happened!', description='Failed to execute command! The correct usage for this command is +ban [mention user] [reason]\n**Examples:**\n+ban @wazzup#4253 underage!!!\n+ban @supaclan#9688 breaking rules and not stopping\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        e.set_footer(text='If that does\'t work, then there must be an error - you cannot ban me or the owners!')
        await context.messsage.channel.send(embed=e)

@client.command(name='warn', pass_content=True)
@commands.has_permissions(administrator=True)
async def warn(context, member: discord.Member, *, reason=None):
    try:
        reason = reason
        user = context.message.author.name
        wEmbed = discord.Embed(title='Warning!', description=f'This is a one time warning, {member.mention}. Please stop '+str(reason), color=0xFF0000)
        embed0 = discord.Embed(title='Warning Stats', description=f'Username: {member.mention}\nReason for warn: '+str(reason)+'\nWarned by: '+user, color=0xFF0000)
        await context.message.channel.send(embed=wEmbed)
        await context.message.channel.send(embed=embed0)
        await member.send('Dude, follow the rules! We ain\'t messin\' around here! :angry: ')
    except:
        errorEmbed = discord.Embed(title='Error: Something Unexpected Happened!', description='Sorry failed to execute this command. The correct usage of this command is +warn [user][reason]\n**Examples:**\n+warn @wazzup$4253 not using channels correctly\n+warn @supaclan#9688 cussing\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        errorEmbed.set_footer(text='If that does\'t work, then the specified user probably has blocked me, preventing me from sending DMs to him!')
        await context.message.channel.send(embed=errorEmbed)

@client.command(name='confirm', pass_content=True)
@commands.has_permissions(administrator=True)
async def confirm(context, *, member: discord.Member, message_id):
    try:
        embed2 = discord.Embed(title='Yay! You have been verified!', descprition='Have fun in the Gamer House!', color =0x00FF00)
        cEmbed = discord.Embed(title='Confirming Verification', color=0x00FF00)
        cEmbed.add_field(name='We are confirming your answers...', value='Please wait while we process...')
        await context.message.channel.send(embed=cEmbed)
        time.sleep(8)
        await member.send('Welcome to the Gamer House! You have been verified! Now, it is time to have a blast! :partying_face: ')
        await context.message.channel.send(embed=embed2)
    except:
        errorEmbed = discord.Embed(title='Error: Something Unexpected Happened!', description='Sorry failed to execute this command. The correct usage of this command is +confirm [user][message id]\n**Examples:**\n+confirm @wazzup$4253 823853973761032193\n+confirm @supaclan#9688 823855937567326268\n\nIf you think that was a mistake, contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432 in https://discord.gg/SQfteTVKnY', color=0xFF0000)
        errorEmbed.set_footer(text='If that does\'t work, then the specified user probably has blocked me, preventing me from sending DMs to him!')
        await context.message.channel.send(embed=errorEmbed)

@client.command(name='close', pass_content=True)
@commands.has_permissions(administrator=True)
async def close(context, message_id, *, reason):
    reason = reason
    closeEmbed = discord.Embed(title='Report Case Closed!', description='The report case has been closed because '+str(reason), color=0xFF0000)
    await context.message.channel.send(embed=closeEmbed)

@client.command(name='override', pass_content = True)
@commands.has_permissions(administrator=True)
async def override(context, member: discord.Member, *,message_id):
    await context.message.channel.send('Please wait, setting up override...')
    oEmbed = discord.Embed(title='Overriding Verification Process', description='This user will not need to go through the verification process again!', color=0x00FFFF)
    time.sleep(5)
    await context.message.channel.send(embed=oEmbed)
    time.sleep(8)
    await context.message.channel.send(f'User {member.mention}\'s verification process has been overrided successfully!')




























#Fun Commands

    
@client.command(name='guilds')
async def servers(ctx):
    await ctx.send(f"This bot is in {len(client.guilds)} guilds (servers)! Keep inviting it! ")

    


@client.command(name='rickroll')
async def rickroll(context):
    rickrollEmbed = discord.Embed(title="Rickroll Link Generated", description="Go try it on your friends", color=0x00FF000)
    rickrollEmbed.set_author(name="Rickroller")
    rickrollEmbed.add_field(name='Minecraft Mod Rickroll Link', value="https://www.thisworldthesedays.com/minecraft-mod-download-for-pc-for-free.html\n\nOR")
    rickrollEmbed.add_field(name='among_us Airship Map Update Date', value="https://www.latlmes.com/breaking/airship-map-among-us-update-revealed-1\n\nOR")
    rickrollEmbed.add_field(name='Free Discord Nitro Gift!', value='https://discordgift.site/qYdLLCnv7KYFsKVL\n\nANOTHER')
    rickrollEmbed.add_field(name='Unlimited Free Robux!', value="https://www.tomorrowtides.com/unlimited-robux-must-see.html")
    rickrollEmbed.set_footer(text='Need more links? go make your own rickrolls: https://www.secretrickroll.com/')
    await context.message.channel.send(embed=rickrollEmbed)



@client.command(name='spam', pass_content=True)
async def spam(context, member: discord.Member, *, message):
    try:
        await context.message.channel.send('Starting to spam!')
        await member.send('Hahah you are gonna get spammed!')
        time.sleep(10)
        times = 0
        while times < 76:
            await member.send(message)
            times = times + 1
        await member.send('The spam is over! **Whew!**\nGo use +spam to get them back!')
        await context.message.author.send('OK, the spam is over, but brace yourself for revenge!')
    except:
        errorEmbed = discord.Embed(title='Error: Something Unexpected Happened', description='Sorry failed to execute this command. The correct usage of this command is +spam [user][message]\n**Examples:**\n+spam @worrybro#9999 hola amigo\n+spam @curryfried#2433 gimme some frieds! If you think this is a mistake, go to https://discord.gg/VkhkArw36Nc and contact 𝖎𝖓𝖛𝖎𝖘𝖎𝖇𝖎𝖑𝖎𝖙𝖞#6432.', color=0xFF0000)
        errorEmbed.set_footer(text='If that doesn\'t work, then the specified user probably blocked me, so I could not DM them.')
        await context.message.channel.send(embed=errorEmbed)



#Rock Paper Scissors
@client.command(name='rock')
async def rock(context):
    await context.message.channel.send('Oh, so you challenge me to rock-paper-scissors? You have NO CHANCE!')
    time.sleep(1)
    list1 = ['rock','paper','scissors']
    move = random.choice(list1)
    await context.message.channel.send('I chose '+str(move)+'!')
    if move == 'paper':
        time.sleep(1)
        await context.message.channel.send(':laughing: HAHAHA you lost!  ')
    elif move == 'scissors':
        time.sleep(1)
        await context.message.channel.send('Dang you won... :slight_frown: ')
    else:
        time.sleep(1)
        await context.message.channel.send('Tie game...? :neutral_face: ')
    


@client.command(name='paper')
async def paper(context):
    await context.message.channel.send('Oh, so you challenge me to rock-paper-scissors? You have NO CHANCE!')
    time.sleep(1)
    list1 = ['rock','paper','scissors']
    move = random.choice(list1)
    await context.message.channel.send('I chose '+str(move)+'!')
    if move == 'scissors':
        time.sleep(1)
        await context.message.channel.send(':laughing: HAHAHA you lost! ')
    elif move == 'rock':
        time.sleep(1)
        await context.message.channel.send('Dang you won... :slight_frown:  ')
    else:
        time.sleep(1)
        await context.message.channel.send('Tie game...? :neutral_face: ')
    



@client.command(name='scissors')
async def scissors(context):
    await context.message.channel.send('Oh, so you challenge me to rock-paper-scissors? You have NO CHANCE!')
    time.sleep(1)
    list1 = ['rock','paper','scissors']
    move = random.choice(list1)
    await context.message.channel.send('I chose '+str(move)+'!')
    if move == 'rock':
        time.sleep(1)
        await context.message.channel.send(':laughing: HAHAHA you lost! ')
    elif move == 'paper':
        time.sleep(1)
        await context.message.channel.send('Dang you won... :slight_frown:  ')
    else:
        time.sleep(1)
        await context.message.channel.send('Tie game...? :neutral_face: ')



























# Run the client on the server
client.run('BOT TOKEN HIDDEN FOR SAFETY REASONS')









'''
NOTE: THIS CODE IS COPYRIGHTED TO THE DISORD BLUE JAY BOT DEVELOPERS. ANY COPYING, TRANSMITTING, OR FORKING THE CODE TO ANOTHER REPOSITORY AND MAKING IT AS YOUR OWN BOT IS ILLEGAL')
