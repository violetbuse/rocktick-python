# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CronUpdateParams", "Request"]


class CronUpdateParams(TypedDict, total=False):
    max_response_bytes: Optional[int]

    max_retries: Optional[int]

    region: Optional[str]

    request: Optional[Request]

    schedule: Optional[str]

    timeout_ms: Optional[int]


class Request(TypedDict, total=False):
    headers: Required[Dict[str, str]]

    method: Required[str]

    url: Required[str]

    body: Optional[str]
