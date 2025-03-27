from ._base import BaseService


class ProfilesService(BaseService):

    def update_profile_proxy(self, profile_id: str, data: dict):
        return self._client._put(f"/profiles/{profile_id}/proxy", data)

    def batch_update_proxy(self, data: dict):
        return self._client._put("/profiles/proxy/batch", data)

    def reset_profile_proxy(self, profile_id: str):
        return self._client._delete(f"/profiles/{profile_id}/proxy")

    def batch_reset_profile_proxy(self, profile_ids: list[str]):
        return self._client._delete(f"/profiles/proxy/batch", profile_ids)

    def create_profile_tags(self, profile_id: str, data: list[dict]):
        return self._client._post(f"/profiles/{profile_id}/tags", data)

    def batch_create_profile_tags(self, data: dict):
        return self._client._post(f"/profiles/tags/batch", data)

    def update_profile_tags(self, profile_id: str, data: list[dict]):
        return self._client._put(f"/profiles/{profile_id}/tags", data)

    def batch_update_profile_tags(self, data: dict):
        return self._client._put(f"/profiles/tags/batch", data)

    def clear_profile_tags(self, profile_id: str):
        return self._client._delete(f"/profiles/{profile_id}/tags")

    def batch_clear_profile_tags(self, profile_ids: list[str]):
        return self._client._delete(f"/profiles/tags/batch", profile_ids)

    def get_profile_tags(self):
        return self._client._get(f"/profiles/tags")

    def create_profile(self, data: dict):
        return self._client._post(f"/profiles", data)

    def delete_profiles(self, profile_ids: list[str]):
        return self._client._delete(f"/profiles", profile_ids)

    def delete_profile(self, profile_id: str):
        return self._client._delete(f"/profiles/{profile_id}")

    def get_profiles(self, data: dict | None = None):
        return self._client._get(f"/profiles", data)
