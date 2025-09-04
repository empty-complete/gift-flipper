"""
This file is taken from
https://github.com/aiogram/aiogram/blob/dev-3.x/tests/mocked_bot.py
(commit 74e00a30b12a2adb47237079bb554f15755ec604)
with slight modifications
"""

from collections import deque
from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING, Any

from aiogram import Bot
from aiogram.client.session.base import BaseSession
from aiogram.methods import TelegramMethod
from aiogram.methods.base import Response, TelegramType
from aiogram.types import UNSET_PARSE_MODE, ResponseParameters, User


class MockedSession(BaseSession):
    def __init__(self) -> None:
        super().__init__()
        self.responses: deque[Response[Any]] = deque()
        self.requests: deque[TelegramMethod[Any]] = deque()
        self.closed = True

    def add_result(self, response: Response[TelegramType]) -> Response[TelegramType]:
        self.responses.append(response)
        return response

    def get_request(self) -> TelegramMethod[Any]:
        return self.requests.pop()

    async def close(self):
        self.closed = True

    async def make_request(
        self,
        bot: Bot,
        method: TelegramMethod[TelegramType],
        timeout: int | None = UNSET_PARSE_MODE,
    ) -> Any:
        self.closed = False
        self.requests.append(method)
        response = self.responses.pop()
        self.check_response(
            bot=bot,
            method=method,
            status_code=response.error_code or 400,
            content=response.model_dump_json(),
        )
        return response.result

    async def stream_content(
        self,
        url: str,
        headers: dict[str, Any] | None = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:  # noqa: UP043
        yield b""


class MockedBot(Bot):
    if TYPE_CHECKING:
        session: MockedSession

    def __init__(self, **kwargs) -> None:
        super().__init__(kwargs.pop("token", "42:TEST"), session=MockedSession(), **kwargs)
        self._me = User(
            id=self.id,
            is_bot=True,
            first_name="FirstName",
            last_name="LastName",
            username="tbot",
            language_code="en-US",
        )

    def add_result_for(
        self,
        method: type[TelegramMethod[TelegramType]],
        ok: bool,
        result: TelegramType | None = None,
        description: str | None = None,
        error_code: int = 200,
        migrate_to_chat_id: int | None = None,
        retry_after: int | None = None,
    ) -> Response[TelegramType]:
        response: Response[TelegramType] = Response(
            ok=ok,
            result=result,
            description=description,
            error_code=error_code,
            parameters=ResponseParameters(
                migrate_to_chat_id=migrate_to_chat_id,
                retry_after=retry_after,
            ),
        )
        self.session.add_result(response)
        return response

    def get_request(self) -> TelegramMethod[Any]:
        return self.session.get_request()
