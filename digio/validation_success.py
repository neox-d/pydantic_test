from __future__ import annotations

from digio.request import Model as RequestModel
from digio.response import Model as ResponseModel


request_external_data = {
    "file_name": "agreement.pdf",
    "file_data": "base64encodedcontent",
    "will_self_sign": False,
    "expire_in_days": 7,
    "callback": "https://example.com/webhooks/digio",
    "comment": "Pydantic validation success sample",
    "display_on_page": "first",
    "notify_signers": True,
    "customer_notification_mode": "ALL",
    "signature_type": "aadhaar",
    "estamp_request": {
        "tags": {"loan_amount": 100000},
        "note_content": "Please sign within 7 days",
        "note_on_page": "last",
        "sign_on_page": "last",
    },
    "sign_coordinates": {
        "signer_1": {
            "1": [
                {"llx": 100, "lly": 150, "urx": 250, "ury": 220},
            ]
        }
    },
    "signature_verification": {
        "signer_1": {
            "abortOnFail": True,
            "maxAttempt": 2,
            "rules": [
                {
                    "operation": "AND",
                    "conditions": [
                        {
                            "field": "NAME",
                            "matchType": "FUZZY",
                            "value": "John Doe",
                            "threshold": 80,
                        }
                    ],
                }
            ],
        }
    },
    "signers": [
        {
            "identifier": "signer_1",
            "name": "John Doe",
            "reason": "Loan agreement signing",
            "sign_type": "aadhaar",
            "signature_mode": "otp",
            "index": 1,
            "signing_addons": [
                {"type": "geo_location", "optional": True},
            ],
        }
    ],
    "sequential": True,
    "send_sign_link": True,
    "include_authentication_url": True,
    "reference_id": "REF-001",
}

request_model = RequestModel(**request_external_data)

print(request_model.file_name)
print(request_model.signers[0].identifier if request_model.signers else None)
print(request_model.model_dump())


response_external_data = {
    "id": "DOC_123",
    "is_agreement": True,
    "agreement_type": "outbound",
    "agreement_status": "requested",
    "file_name": "agreement.pdf",
    "created_at": "2026-03-18T06:30:00Z",
    "no_of_pages": 2,
    "self_signed": False,
    "signing_parties": [
        {
            "name": "John Doe",
            "status": "requested",
            "type": "signatory",
            "signature_type": "aadhaar",
            "signature_mode": "otp",
            "identifier": "signer_1",
            "expire_on": "2026-03-25T06:30:00Z",
            "authentication_url": "https://example.com/auth/sign/signer_1",
        }
    ],
    "sign_request_details": {
        "name": "Loan Agreement",
        "requested_on": "2026-03-18T06:30:00Z",
        "expire_on": "2026-03-25T06:30:00Z",
        "identifier": "REQ_001",
        "requester_type": "org",
        "channel": "api",
        "require_full_document_review": False,
    },
    "draft": {
        "file_name": "agreement.pdf",
        "sequential": True,
        "send_sign_link": True,
        "comment": "Draft created",
        "notify_signers": True,
        "display_on_page": "first",
        "signature_verification": {
            "signer_1": {
                "abortOnFail": True,
                "maxAttempt": 2,
                "rules": [
                    {
                        "operation": "AND",
                        "conditions": [
                            {
                                "field": "NAME",
                                "matchType": "FUZZY",
                                "value": "John Doe",
                                "threshold": 80,
                            }
                        ],
                    }
                ],
            }
        },
        "reference_id": "REF-001",
        "createdAt": "2026-03-18T06:30:00Z",
        "updatedAt": "2026-03-18T06:31:00Z",
    },
}

response_model = ResponseModel(**response_external_data)

print(response_model.id)
print(response_model.created_at)
print(response_model.model_dump())
