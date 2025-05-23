#  Copyright (c) 2022 @TheRiZoeL - RiZoeL
# Telegram Ban All Bot 
# Creator - RiZoeL

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


logging.basicConfig(level=logging.INFO)

print("𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆.....")

Riz = TelegramClient('Riz', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm On 𝐀𝐉𝐄𝐄𝐓 𓆩𝗫𓆪 𝐑𝐎𝐁𝐎𝐓** \n\n __Pong__ !! `{ms}` ms")


@Riz.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝐀𝐁𝐄 𝐂𝐇𝐔𝐓𝐓𝐈𝐘𝐄 🤪 !! 𝐘𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐆𝐑𝐎𝐔𝐏 𝐌𝐄 𝐉𝐀 𝐊𝐄 𝐔𝐒𝐄 𝐊𝐀𝐑 𝐏𝐇𝐈𝐑 𝐃𝐄𝐊𝐇𝐎 𝐊𝐌𝐀𝐀𝐋 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 𝐊𝐄 𝐁𝐎𝐓 𝐊𝐀 🥳🥳🥳🥳."
         await event.reply(Reply)
     else:
         await event.delete()
         RiZ = await event.get_chat()
         RiZoeLop = await event.client.get_me()
         admin = RiZ.admin_rights
         creator = RiZ.creator
         if not admin and not creator:
              return await event.reply("𝐂𝐇𝐔𝐓𝐈𝐘𝐄𝐄 𝐑𝐈𝐆𝐇𝐓𝐒 𝐓𝐎 𝐃𝐈𝐋𝐀 👿👿👿, 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 😍 𝐊𝐀 𝐁𝐎𝐓 𝐀𝐀𝐈𝐒𝐄 𝐊𝐀𝐀𝐌 𝐍𝐀𝐇𝐈 𝐊𝐀𝐑𝐓𝐀 😊😌😌😌!!")
         RiZoeL = await Riz.send_message(event.chat_id, "**𝐇𝐄𝐇𝐄𝐄𝐄 !! 𝐌𝐀𝐈 𝐉𝐈𝐍𝐃𝐀 𝐇𝐔 😍😍**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         kimk = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
                if user.id not in admins_id:
                    await event.client.kick_participant(event.chat_id, user.id)
                    kimk += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
         await RiZoeL.edit(f"**𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 🥵 𝐍𝐄 𝐂𝐇𝐎𝐃𝐃𝐃 👉👉👌 𝐊𝐄 𝐂𝐇𝐇𝐎𝐑 𝐃𝐈𝐘𝐀 😋😋😋** `{kimk}` \n **Total:** `{all}`")
    

@Riz.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         RiZ = await event.get_chat()
         RiZoeLop = await event.client.get_me()
         admin = RiZ.admin_rights
         creator = RiZ.creator
         if not admin and not creator:
              return await event.reply("𝐂𝐇𝐔𝐓𝐈𝐘𝐄𝐄 𝐑𝐈𝐆𝐇𝐓𝐒 𝐓𝐎 𝐃𝐈𝐋𝐀 👿👿👿, 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 😍 𝐊𝐀 𝐁𝐎𝐓 𝐀𝐀𝐈𝐒𝐄 𝐊𝐀𝐀𝐌 𝐍𝐀𝐇𝐈 𝐊𝐀𝐑𝐓𝐀 😊😌😌😌!!")
         RiZoeL = await Riz.send_message(event.chat_id, "**𝐇𝐄𝐇𝐄𝐄𝐄 !! 𝐌𝐀𝐈 𝐉𝐈𝐍𝐃𝐀 𝐇𝐔 😍😍**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                   print(str(e))
                   await asyncio.sleep(0.1)
         await RiZoeL.edit(f"**𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 🥵 𝐍𝐄 𝐂𝐇𝐎𝐃𝐃𝐃 👉👉👌 𝐊𝐄 𝐂𝐇𝐇𝐎𝐑 𝐃𝐈𝐘𝐀 😋😋😋 ! \n\n Banned Users:** `{bann}` \n **Total Users:** `{all}`")

    
@Riz.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝐂𝐇𝐔𝐓𝐈𝐘𝐄𝐄 𝐑𝐈𝐆𝐇𝐓𝐒 𝐓𝐎 𝐃𝐈𝐋𝐀 👿👿👿, 𝐀𝐉𝐄𝐄𝐓 𝐏𝐀𝐏𝐀 😍 𝐊𝐀 𝐁𝐎𝐓 𝐀𝐀𝐈𝐒𝐄 𝐊𝐀𝐀𝐌 𝐍𝐀𝐇𝐈 𝐊𝐀𝐑𝐓𝐀 😊😌😌😌!!."
         await event.reply(Reply)
     else:
         msg = await event.reply("Searching Participant Lists.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleeping for {ex.seconds} seconds")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))


@Riz.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
          

@Riz.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Restarting__ babu !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Riz.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("Your Ban All Bot Deployed Successfully ✅")

Riz.run_until_disconnected()
