from vkbottle.bot import BotLabeler, Message, rules, Bot
from vkbottle_types.objects import MessagesConversation
from vkbottle import API
from __future__ import annotations
from typing import Dict
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session
from sqlalchemy.orm.collections import attribute_keyed_dict
class ChatInfoRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        chats_info = await message.ctx_api.messages.get_conversations_by_id(message.peer_id)
        return {"chat": chats_info.items[0]}




for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=event.obj.text)

@bot.on.message(mention=True)
async def mention_handler(message: Message):
    await message.answer(f'привет!')
if message == 'привет':
    blasthack(id, 'Привет, я бот!')

@chat_labeler.message(text="начать поиск")
async def To_start_searching(message: Message, chat: MessagesConversation):
    await message.ctx_api.messages.remove_chat_user(message.chat_id, message.from_id)

@chat_labeler.message(text="показать избранных")
async def show_favorites(message: Message, chat: MessagesConversation):
    await message.ctx_api.messages.remove_chat_user(message.chat_id, message.from_id)

async def _request(
            self,
            method: str,
            str_or_url: StrOrURL,
            *,
            params: Optional[Mapping[str, str]] = None,
            data: Any = None,
            json: Any = None,
            cookies: Optional[LooseCookies] = None,
            headers: Optional[LooseHeaders] = None,
            skip_auto_headers: Optional[Iterable[str]] = None,
            auth: Optional[BasicAuth] = None,
            allow_redirects: bool = True,
            max_redirects: int = 10,
            compress: Optional[str] = None,
            chunked: Optional[bool] = None,
            expect100: bool = False,
            raise_for_status: Optional[bool] = None,
            read_until_eof: bool = True,
            proxy: Optional[StrOrURL] = None,
            proxy_auth: Optional[BasicAuth] = None,
            timeout: Union[ClientTimeout, object] = sentinel,
            verify_ssl: Optional[bool] = None,
            fingerprint: Optional[bytes] = None,
            ssl_context: Optional[SSLContext] = None,
            ssl: Optional[Union[SSLContext, bool, Fingerprint]] = None,
            proxy_headers: Optional[LooseHeaders] = None,
            trace_request_ctx: Optional[SimpleNamespace] = None,
            read_bufsize: Optional[int] = None,
    ) -> ClientResponse:



        if self.closed:
            raise RuntimeError("Сессия закрыта")

        ssl = _merge_ssl_params(ssl, verify_ssl, ssl_context, fingerprint)

        if data is not None and json is not None:
            raise ValueError(
                "data and json parameters can not be used at the same time"
            )
        elif json is not None:
            data = payload.JsonPayload(json, dumps=self._json_serialize)

        if not isinstance(chunked, bool) and chunked is not None:
            warnings.warn("Chunk size is deprecated #1615", DeprecationWarning)
node = TreeNode('rootnode')
node.append('node1')
node.append('node3')
session.add(node)
session.commit()

dump_tree(node)
class Base(DeclarativeBase):
    pass


class TreeNode(MappedAsDataclass, Base):
    __tablename__ = "tree"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("tree.id"), init=False
    )
    name: Mapped[str]

    children: Mapped[Dict[str, TreeNode]] = relationship(
        cascade="all, delete-orphan",
        back_populates="parent",
        collection_class=attribute_keyed_dict("name"),
        init=False,
        repr=False,
    )

    parent: Mapped[Optional[TreeNode]] = relationship(
        back_populates="children", remote_side=id, default=None
    )

    def dump(self, _indent: int = 0) -> str:
        return (
            "   " * _indent
            + repr(self)
            + "\n"
            + "".join([c.dump(_indent + 1) for c in self.children.values()])
        )


if __name__ == "__main__":
    engine = create_engine("sqlite://", echo=True)

    print("Creating Tree Table:")

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        node = TreeNode("rootnode")
        TreeNode("node1", parent=node)
        TreeNode("node3", parent=node)

        node2 = TreeNode("node2")
        TreeNode("subnode1", parent=node2)
        node.children["node2"] = node2
        TreeNode("subnode2", parent=node.children["node2"])

        print(f"Created new tree structure:\n{node.dump()}")

        print("flush + commit:")

        session.add(node)
        session.commit()

        print(f"Tree after save:\n{node.dump()}")

        session.add_all(
            [
                TreeNode("node4", parent=node),
                TreeNode("subnode3", parent=node.children["node4"]),
                TreeNode("subnode4", parent=node.children["node4"]),
                TreeNode(
                    "subsubnode1",
                    parent=node.children["node4"].children["subnode3"],
                ),
            ]
        )


        del node.children["node1"]

        print("Removed node1.  flush + commit:")
        session.commit()

        print("Tree after save, will unexpire all nodes:\n")
        print(f"{node.dump()}")

    with Session(engine) as session:
        print(
            "Perform a full select of the root node, eagerly loading "
            "up to a depth of four"
        )
        node = session.scalars(
            select(TreeNode)
            .options(selectinload(TreeNode.children, recursion_depth=4))
            .filter(TreeNode.name == "rootnode")
        ).one()

        print(f"Full Tree:\n{node.dump()}")

        print("Marking root node as deleted, flush + commit:")