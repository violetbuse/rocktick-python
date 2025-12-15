# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Execution", "Request", "Response"]


class Request(BaseModel):
    headers: Dict[str, str]

    method: str

    url: str

    body: Optional[str] = None


class Response(BaseModel):
    body: str

    headers: Dict[str, str]

    status: int


class Execution(BaseModel):
    id: str

    max_retries: int

    region: str

    request: Request

    scheduled_at: int

    cron_job_id: Optional[str] = None

    executed_at: Optional[int] = None

    max_response_bytes: Optional[int] = None

    one_off_job_id: Optional[str] = None

    response: Optional[Response] = None

    response_error: Optional[str] = None

    retry_for: Optional[str] = None

    success: Optional[bool] = None

    tenant_id: Optional[str] = None

    timeout_ms: Optional[int] = None
