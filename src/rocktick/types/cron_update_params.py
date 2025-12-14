# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .request_param import RequestParam

__all__ = ["CronUpdateParams"]


class CronUpdateParams(TypedDict, total=False):
    max_response_bytes: Optional[int]

    max_retries: Optional[int]

    region: Optional[str]

    request: Optional[RequestParam]

    schedule: Optional[str]

    timeout_ms: Optional[int]
