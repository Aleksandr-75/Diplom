from .chat import chat_labeler
from .admin import admin_labeler
from .ping import labeler


__all__ = ("admin_labeler", "chat_labeler", "labeler")
from vkbottle.dispatch.rules.base import CommandRule
from typing import Tuple

@bot.on.message(CommandRule("say", ["!", "/"], 1))
async def say_handler(message: Message, args: Tuple[str]):
    await message.answer(f"<<{args[0]}>>")
