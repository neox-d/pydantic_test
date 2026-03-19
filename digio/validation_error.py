from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import ValidationError


if TYPE_CHECKING:
    from digio.request import Model as RequestModel
    from digio.response import Model as ResponseModel
else:
    _HERE = Path(__file__).resolve().parent
    if str(_HERE) not in sys.path:
        sys.path.insert(0, str(_HERE))

    from request import Model as RequestModel
    from response import Model as ResponseModel


request_invalid_data = {
    "file_name": 123,  # should be str
    "file_data": None,  # should be str
    "display_on_page": "middle",  # invalid enum
    "expire_in_days": "seven",  # should be int
    "sign_coordinates": {
        "signer_1": {"1": [{"llx": "x", "lly": 0, "urx": 10, "ury": 10}]}
    },
    "signature_verification": {
        "signer_1": {
            "abortOnFail": "yes",  # should be bool
            "maxAttempt": "two",  # should be int
            "rules": [
                {
                    "operation": "XOR",  # invalid enum
                    "conditions": [
                        {
                            "field": "FULL_NAME",  # invalid enum
                            "matchType": "CLOSE",  # invalid enum
                            "value": 999,  # should be str
                        }
                    ],
                }
            ],
        }
    },
    "signers": [
        {
            "name": "John Doe",
            "sign_type": "aadhaar",
            "signature_mode": "otp",
        }
    ],
}

try:
    RequestModel(**request_invalid_data)
except ValidationError as e:
    print(e.errors())
    """
    Example output (truncated):
    [
        {
            'type': 'string_type',
            'loc': ('file_name',),
            'msg': 'Input should be a valid string',
            'input': 123,
            ...
        },
        {
            'type': 'string_type',
            'loc': ('file_data',),
            'msg': 'Input should be a valid string',
            'input': None,
            ...
        },
        {
            'type': 'enum',
            'loc': ('display_on_page',),
            'msg': "Input should be 'first', 'last', 'all' or 'custom'",
            'input': 'middle',
            ...
        },
        ...
    ]
    """


response_invalid_data = {
    "agreement_type": "sideways",  # invalid enum
    "agreement_status": "done",  # invalid enum
    "created_at": "2026-03-18T06:30:00",  # naive datetime, should be timezone-aware
    "no_of_pages": "two",  # should be int
    "sign_request_details": {
        "requested_on": "not a datetime",
        "channel": "pager",  # invalid enum
    },
}

try:
    ResponseModel(**response_invalid_data)
except ValidationError as e:
    print(e.errors())
    """
    Example output (truncated):
    [
        {
            'type': 'enum',
            'loc': ('agreement_type',),
            'msg': "Input should be 'inbound' or 'outbound'",
            'input': 'sideways',
            ...
        },
        {
            'type': 'timezone_aware',
            'loc': ('created_at',),
            'msg': 'Input should have timezone info',
            'input': '2026-03-18T06:30:00',
            ...
        },
        ...
    ]
    """
