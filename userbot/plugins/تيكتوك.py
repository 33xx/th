from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import jmthon, CMD_HELP
#

@jmthon.on(admin_cmd(pattern="تيكتوك(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r_link = event.pattern_match.group(1)
    if ".com" not in r_link:
        await event.edit("**♰ يجب وضع رابط الفيديو مع الامر اولا **")
    else:
        await event.edit("**♰ تتم المعالجة انتظر قليلا**")
    chat = "@Q5MBOT"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(r_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ كتابة فريق ريك  @K4KK44 """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("♰ الغـي حـظر هـذا البـوت و حـاول مجـددا @Q5MBOT")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id]
        )
        await event.delete()


# TELEGRAM   :  @K4KK44  - @HvvHH
CMD_HELP.update(
    {
        "تيكتوك":".تيكتوك <رابط فيد>\n اكتب الامر مع رابط الفيديو من تيكتوك لتحميله وارساله لك" 
        }
        )
