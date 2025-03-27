from ._base import BaseService


class BrowsersService(BaseService):

    def start_browser(self, profile_id: str):
        return self._client._post(f"/browsers/{profile_id}")

    def start_browsers(self, profile_ids: list[str]):
        return self._client._post(f"/browsers", profile_ids)

    def start_once_browser(self, data: dict):
        return self._client._post(f"/browsers/once", data)

    def stop_browser(self, profile_id: str):
        return self._client._delete(f"/browsers/{profile_id}")

    def stop_browsers(self, profile_ids: list[str]):
        return self._client._delete(f"/browsers", profile_ids)

    def get_browsers(self, status: str | None = None):
        return self._client._get(f"/browsers", {"status": status})

    def get_browser_pages(self, profile_id: str):
        return self._client._get(f"/browsers/{profile_id}/pages")

    def get_browser_debugger(self, profile_id: str):
        return self._client._get(f"/browsers/{profile_id}/debugger")
