# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .request_param import RequestParam

__all__ = ["CronCreateParams"]


class CronCreateParams(TypedDict, total=False):
    request: Required[RequestParam]

    schedule: Required[str]

    max_response_bytes: Optional[int]

    max_retries: Optional[int]

    region: Optional[str]

    timeout_ms: Optional[int]
