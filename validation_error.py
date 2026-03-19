from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError


from request import (
    Field,
    File,
    MultipleStampSery,
    StampUpload,
    DocumentDetail,
    StampDatum,
    Participant,
    NeslParty,
    NeslSecurity,
    NeslData,
    WorkflowPaymentCollectionConfig,
    GpsConfig,
    AadhaarConfig,
    OfflineSignConfig,
    DscConfig,
    NeslConfig,
    Invitee,
    CcItem,
    Model as RequestModel,
)

from response import (
    Message,
    Invitee as ResponseInvitee,
    Data,
    Model as ResponseModel,
)


request_invalid_data = {
    "profileId": 12345,
    "file": {
        "name": "test.pdf",
        "file": "base64encodedcontent",
        "fields": [
            {
                "id": "field1",
                "name": "Field 1",
                "type": "text",
                "value": "Test Value",
                "checked": "not a bool",
                "multiple": 123,
                "width": "100",
                "height": "50",
                "required": "yes",
            }
        ],
        "autoGroupedFieldsFill": "true",
        "additionalFiles": "not none",
    },
    "stampSeries": "SERIES001",
    "multipleStampSeries": [{"stampSeries": "STAMP001", "seriesQuantity": "ten"}],
    "seriesGroup": "GROUP1",
    "stampValue": "500",
    "stampUpload": {
        "state": "MAHARASHTRA",
        "denomination": 500.50,
        "firstPartyName": "Party A",
        "secondPartyName": "Party B",
        "stampSerial": "SERIAL123",
        "stampFile": "base64encodedfile",
    },
    "revenueStampSeries": "REV001",
    "revenueStampQuantity": -5,
    "neslData": {
        "documentDetail": {
            "loanNumber": "LN001",
            "sanctionNumber": "SN001",
            "registrationType": "TYPE1",
            "state": "MAHARASHTRA",
            "branchName": "Main Branch",
            "branchAddress": "Address Line 1",
            "dateOfSanction": "2024-01-01",
            "emiAmount": "5000",
            "rateOfInterest": "10.5",
            "sanctionAmount": "100000",
            "tenure": "24",
            "typeOfDebt": "secured",
            "accountClosedFlag": "N",
            "fundType": "fresh",
            "sanctionCurrency": "INVALID",
            "creditSubtype": "personal",
            "facilityName": "Personal Loan",
            "amountOverdue": "0",
            "otherChargeAmount": "0",
            "debtStartDate": "2024-01-01",
            "interestAmount": "5000",
            "oldDebtRefNo": "",
            "principalOutstanding": "100000",
            "loanRemark": "Approved",
            "totalOutstandingAmount": "105000",
            "creditorBusinessUnit": "BU001",
            "drawingPower": "50000",
            "daysPastDue": "0",
            "docRefNo": "DOC001",
            "expiryDateEbg": "2025-12-31",
            "claimExpiryDate": "2025-12-31",
            "contractRefNo": "CONTRACT001",
            "vendorCode": "VC001",
            "portalId": "PORTAL001",
            "event": "created",
        },
        "stampData": [
            {
                "firstParty": "Party A",
                "secondParty": "Party B",
                "stampDutyAmount": "invalid",
                "considerationPrice": "10000",
                "descriptionOfDocument": "Loan Agreement",
                "stampDutyPaidBy": "borrower",
                "articleCode": "ART001",
                "firstPartyPin": "41100",
                "secondPartyPin": "411002",
                "firstPartyOVDType": "aadhaar",
                "firstPartyOVDValue": "123456789012",
                "secondPartyOVDType": "aadhaar",
                "secondPartyOVDValue": "123456789013",
            }
        ],
        "participants": [
            {
                "fullName": "John Doe",
                "contactPersonName": "John",
                "contactRelation": "self",
                "emailId": "invalid-email",
                "mobileNumber": "123",
                "dob": "not a date",
                "legalConstitution": "individual",
                "alternateEmailId": "john.alt@example.com",
                "alternateMobileNumber": "9876543211",
                "officialDocType": "aadhaar",
                "officialDocId": "123456789012",
                "registeredAddress": "Address Line 1",
                "registeredPinCode": "411001",
                "designation": "Borrower",
                "communicationAddress": "Address Line 2",
                "communicationAddressPinCode": "411002",
                "cin": "",
                "kin": "",
                "partyType": "borrower",
                "isIndividual": "yes",
                "signatoryGender": "male",
                "businessUnit": "BU001",
            }
        ],
        "neslParties": [],
        "neslSecurities": [],
    },
    "invitees": [
        {
            "name": 12345,
            "email": "not-an-email",
            "phone": "123",
            "groupId": "GROUP1",
            "groupName": "Group 1",
            "completionThreshold": "100",
            "organizationName": "Org 1",
            "defaultLanguageSelect": "en",
            "faceMatchImage": "base64image",
            "workflowPaymentCollectionConfig": {
                "amount": -100,
            },
            "gpsConfig": {
                "applyLocationRestriction": "yes",
                "allowedLatitude": "invalid",
                "allowedLongitude": "72.8777",
                "permissibleRadius": -500,
                "applyLocationAccuracy": "maybe",
                "accuracyThreshold": "high",
            },
            "aadhaarConfig": {
                "verifyName": "yes",
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyYob": "1990",
                "verifyTitle": "Mr",
                "verifyState": "MAHARASHTRA",
                "verifyGender": "M",
            },
            "offlineSignConfig": {
                "mobileNumber": "9876543210",
                "pan": "invalid",
                "signerId": "SIGNER001",
                "verifyName": "true",
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyState": "MAHARASHTRA",
                "verifyYob": "1990",
                "verifyTitle": "Mr",
                "verifyGender": "M",
            },
            "dscConfig": {
                "verifyName": "yes",
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyState": "MAHARASHTRA",
            },
            "neslConfig": {
                "verifyName": "yes",
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyYob": "1990",
                "verifyTitle": "Mr",
                "verifyState": "MAHARASHTRA",
                "verifyGender": "M",
            },
        }
    ],
    "cc": [{"name": "CC User", "email": "not-valid-email"}],
    "irn": 123,
}

try:
    RequestModel(**request_invalid_data)
except ValidationError as e:
    # print(e.errors())
    print(str(e))
    """
    [
        {
            'type': 'string_type',
            'loc': ('profileId',),
            'msg': 'Input should be a valid string',
            'input': 12345,
            'url': 'https://errors.pydantic.dev/2/v/string_type',
        },
        {
            'type': 'bool_type',
            'loc': ('file', 'fields', 0, 'checked'),
            'msg': 'Input should be a valid boolean',
            'input': 'not a bool',
            'url': 'https://errors.pydantic.dev/2/v/bool_type',
        },
        {
            'type': 'int_parsing',
            'loc': ('file', 'fields', 0, 'multiple'),
            'msg': 'Input should be a valid integer',
            'input': 123,
            'url': 'https://errors.pydantic.dev/2/v/int_parsing',
        },
        {
            'type': 'bool_type',
            'loc': ('file', 'autoGroupedFieldsFill'),
            'msg': 'Input should be a valid boolean',
            'input': 'true',
            'url': 'https://errors.pydantic.dev/2/v/bool_type',
        },
        ...
    ]
    """


response_invalid_data = {
    "status": "not an int",
    "messages": [{"code": 123, "message": 456}],
    "data": {
        "documentId": 12345,
        "irn": "IRN001",
        "invitees": [
            {
                "name": 123,
                "email": "invalid",
                "phone": "phone",
                "signUrl": 123,
                "active": "yes",
                "expiryDate": 123,
            }
        ],
    },
}

try:
    ResponseModel(**response_invalid_data)
except ValidationError as e:
    # print(e.errors())
    print(str(e))
    """
    [
        {
            'type': 'int_parsing',
            'loc': ('status',),
            'msg': 'Input should be a valid integer',
            'input': 'not an int',
            'url': 'https://errors.pydantic.dev/2/v/int_parsing',
        },
        {
            'type': 'string_type',
            'loc': ('messages', 0, 'code'),
            'msg': 'Input should be a valid string',
            'input': 123,
            'url': 'https://errors.pydantic.dev/2/v/string_type',
        },
        {
            'type': 'string_type',
            'loc': ('messages', 0, 'message'),
            'msg': 'Input should be a valid string',
            'input': 456,
            'url': 'https://errors.pydantic.dev/2/v/string_type',
        },
        {
            'type': 'string_type',
            'loc': ('data', 'documentId'),
            'msg': 'Input should be a valid string',
            'input': 12345,
            'url': 'https://errors.pydantic.dev/2/v/string_type',
        },
        {
            'type': 'string_type',
            'loc': ('data', 'invitees', 0, 'name'),
            'msg': 'Input should be a valid string',
            'input': 123,
            'url': 'https://errors.pydantic.dev/2/v/string_type',
        },
        {
            'type': 'email_parsing',
            'loc': ('data', 'invitees', 0, 'email'),
            'msg': 'Input should be a valid email address',
            'input': 'invalid',
            'url': 'https://errors.pydantic.dev/2/v/email_parsing',
        },
        ...
    ]
    """
