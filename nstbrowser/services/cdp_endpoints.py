import json

from ._base import BaseService


class CdpEndpointsService(BaseService):

    def connect_browser(self, profile_id: str, config: dict):
        payload = json.dumps(config)
        return self._client._get(f"/connect/{profile_id}", {"config": payload})

    def connect_once_browser(self, config: dict):
        payload = json.dumps(config)
        return self._client._get(f"/connect", {"config": payload})
