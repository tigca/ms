# #️⃣ Module "compliments" by t.me/wavams
# ✅ Only for teagram userbot 
# ⚙️ Commands: .compliments
from pyrogram import Client, types
from .. import loader, utils
import random


@loader.module(name="Compliments")
class ComplimentsMod(loader.Module):
    """👻 Модуль с рандомными комплиментами"""


    @loader.ratelimit
    async def compliments_cmd(self, app: Client, message: types.Message):
        compliments = [
            "Ты лучший!",
            "Не сдавайся!",
            "У тебя все получится!",
            "Ты умный и талантливый!",
            "Ты прекрасен!",
            "Ты делаешь мир лучше!"
        ]
        compliment = random.choice(compliments)
        await utils.answer(message, compliment)
