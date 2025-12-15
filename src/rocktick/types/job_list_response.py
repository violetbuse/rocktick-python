# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .execution import Execution

__all__ = ["JobListResponse", "Request"]


class Request(BaseModel):
    headers: Dict[str, str]

    method: str

    url: str

    body: Optional[str] = None


class JobListResponse(BaseModel):
    id: str

    execute_at: int

    executions: List[Execution]

    max_retries: int

    region: str

    request: Request

    max_response_bytes: Optional[int] = None

    tenant_id: Optional[str] = None

    timeout_ms: Optional[int] = None
