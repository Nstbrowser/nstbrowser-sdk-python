from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nstbrowser import NstbrowserClient


class BaseService:
    def __init__(self, client: "NstbrowserClient"):
        self._client = client
