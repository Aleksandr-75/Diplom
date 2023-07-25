from typing import Union
from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

class MyRule(ABCRule[Message]):
    async def check(self, event: Message) -> Union[dict, bool]:
        ...
