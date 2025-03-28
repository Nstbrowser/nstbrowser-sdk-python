from ._base import BaseService


class LocalsService(BaseService):

    def clear_profile_cache(self, profile_id: str):
        return self._client._delete(f"/local/profiles/{profile_id}")

    def clear_profile_cookies(self, profile_id: str):
        return self._client._delete(f"/local/profiles/{profile_id}/cookies")
