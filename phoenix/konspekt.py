from telethon import events
import phoenix.client
client = phoenix.client.client


@events.register(events.NewMessage(outgoing=True, pattern='\.ملخص'))
async def tconv(event):
    chat = await event.get_chat()
    replied_msg = await event.get_reply_message()
    await event.edit("انتظر...")
    await client.send_message('@Online_Konspekt_Bot', '/start')
    x = await replied_msg.forward_to('@Online_Konspekt_Bot')

    async with client.conversation('@Online_Konspekt_Bot') as conv:
        xx = await conv.get_response(x.id)
        await client.send_read_acknowledge(conv.chat_id)
        await client.send_message(chat, xx)
        await event.message.delete()
