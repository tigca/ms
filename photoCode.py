import requests
import io

from .. import utils, loader
from pyrogram import types, Client

@loader.module('PhotoCode', 'itzlayz', 1.0)
class PhotoCodeMod(loader.Module):
    """Данный модуль превратит код в картинку"""

    async def makephoto_cmd(self, app: Client, message: types.Message, args: str):
        """"""
        app.me = await app.get_me()
        if not args:
            if not (args := message.reply_to_message.text):
                return await utils.answer(
                    message, 
                    '❌ Вы не указали текст или реплай с текстом'
                )

        text = args.rstrip('`').lstrip('`')

        params = 'theme=vsc-dark-plus&language=python&line-numbers=true&background-color=gray'
        url = 'https://code2img.vercel.app/api/to-image?' + params
        
        await message.edit_text(
            '🕒 Подождите...'
        )

        photo = io.BytesIO(
            (
                await utils.run_sync(
                    requests.post, # type: ignore
                    url,
                    headers={"content-type": "text/plain"},
                    data=bytes(text, "utf-8"),
                )
            ).content
        )
        photo.name = "photo.jpg"
        
        await utils.answer(
            message,
            photo,
            photo=True
        )

        await message.edit_text('Готово! ✔')
