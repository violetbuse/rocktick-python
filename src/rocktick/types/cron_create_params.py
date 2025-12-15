# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CronCreateParams", "Request"]


class CronCreateParams(TypedDict, total=False):
    request: Required[Request]

    schedule: Required[str]

    max_response_bytes: Optional[int]

    max_retries: Optional[int]

    region: Optional[str]

    timeout_ms: Optional[int]


class Request(TypedDict, total=False):
    headers: Required[Dict[str, str]]

    method: Required[str]

    url: Required[str]

    body: Optional[str]
