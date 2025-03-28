import inspect
import logging
import requests
from typing import Any, Dict, List, Optional, Union

from . import services

logger = logging.getLogger(__name__)


class NstbrowserClient:
    api_key: str
    api_address: str
    browsers: services.BrowsersService
    profiles: services.ProfilesService
    locals: services.LocalsService
    cdp_endpoints: services.CdpEndpointsService

    def __init__(self, api_key: str, api_address: str = "http://localhost:8848/api/v2"):
        if not api_key:
            raise ValueError("NST ERROR: please input a correct key!")
        self.api_key = api_key
        self.api_address = api_address
        self.browsers = services.BrowsersService(self)
        self.profiles = services.ProfilesService(self)
        self.locals = services.LocalsService(self)
        self.cdp_endpoints = services.CdpEndpointsService(self)

    @property
    def headers(self):
        return {"x-api-key": self.api_key}

    def _request(self, method: str, url: str, **kwargs):
        try:
            logger.debug(
                f"{method.upper()} Request URL: {self.api_address}{url}, kwargs: {kwargs}"
            )
            response = requests.request(
                method, f"{self.api_address}{url}", headers=self.headers, **kwargs
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            caller_frame = inspect.stack()[2]
            caller_method_name = caller_frame.function
            caller_self = caller_frame.frame.f_locals.get("self", None)
            caller_class_name = (
                caller_self.__class__.__name__ if caller_self else "Unknown"
            )

            logger.error(f"Error in [{caller_class_name}.{caller_method_name}]: {e}")
            raise RuntimeError(
                f"Error in [{caller_class_name}.{caller_method_name}]: {e}"
            ) from e

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._request("get", url, params=params)

    def _post(
        self, url: str, data: Optional[Union[Dict[str, Any], List[Any]]] = None
    ) -> Dict[str, Any]:
        return self._request("post", url, json=data)

    def _put(self, url: str, data: Optional[Union[Dict[str, Any], List[Any]]] = None) -> Dict[str, Any]:
        return self._request("put", url, json=data)

    def _delete(
        self, url: str, data: Optional[Union[Dict[str, Any], List[Any]]] = None
    ) -> Dict[str, Any]:
        return self._request("delete", url, json=data)
