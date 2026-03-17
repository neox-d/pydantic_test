from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "signup_ts": "2019-06-01 12:22",
    "tastes": {
        "wine": 9,
        b"cheese": 7,
        "cabbage": "1",
    },
}

user = User(**external_data)

print(user.id)
# > 123
print(user.model_dump())
"""
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
"""

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


request_external_data = {
    "profileId": "12345",
    "file": {
        "name": "test.pdf",
        "file": "base64encodedcontent",
        "fields": [
            {
                "id": "field1",
                "name": "Field 1",
                "type": "text",
                "value": "Test Value",
                "checked": True,
                "multiple": False,
                "width": "100",
                "height": "50",
                "required": True,
            }
        ],
        "autoGroupedFieldsFill": True,
        "additionalFiles": None,
    },
    "stampSeries": "SERIES001",
    "multipleStampSeries": [{"stampSeries": "STAMP001", "seriesQuantity": "10"}],
    "seriesGroup": "GROUP1",
    "stampValue": "500",
    "stampUpload": {
        "state": "MAHARASHTRA",
        "denomination": "500",
        "firstPartyName": "Party A",
        "secondPartyName": "Party B",
        "stampSerial": "SERIAL123",
        "stampFile": "base64encodedfile",
    },
    "revenueStampSeries": "REV001",
    "revenueStampQuantity": "5",
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
            "sanctionCurrency": "INR",
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
                "stampDutyAmount": "500",
                "considerationPrice": "10000",
                "descriptionOfDocument": "Loan Agreement",
                "stampDutyPaidBy": "borrower",
                "articleCode": "ART001",
                "firstPartyPin": "411001",
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
                "emailId": "john@example.com",
                "mobileNumber": "9876543210",
                "dob": "1990-01-01",
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
        "neslParties": [
            {
                "fullName": "Party A",
                "contactPersonName": "Contact Person",
                "contactRelation": "authorized",
                "emailId": "party@example.com",
                "mobileNumber": "9876543210",
                "dob": "1985-01-01",
                "legalConstitution": "company",
                "alternateEmailId": "",
                "alternateMobileNumber": "",
                "officialDocType": "cin",
                "officialDocId": "U12345MH2020PTC123456",
                "registeredAddress": "Registered Address",
                "registeredPinCode": "411001",
                "designation": "Director",
                "communicationAddress": "Communication Address",
                "communicationAddressPinCode": "411002",
                "cin": "U12345MH2020PTC123456",
                "kin": "",
                "partyType": "borrower",
                "isIndividual": "no",
                "signatoryGender": "",
            }
        ],
        "neslSecurities": [
            {
                "securityDescription": "Property Security",
                "assetsType": "immovable",
                "chargeType": "hypothecation",
                "assetId": "ASSET001",
                "doc": "2024-01-01",
                "dov": "2024-01-01",
                "cersaiId": "CERSAI001",
                "rocChargeId": "ROC001",
                "securityValue": "150000",
                "abc": "",
            }
        ],
    },
    "invitees": [
        {
            "name": "Invitee 1",
            "email": "invitee1@example.com",
            "phone": "9876543210",
            "groupId": "GROUP1",
            "groupName": "Group 1",
            "completionThreshold": "100",
            "organizationName": "Org 1",
            "defaultLanguageSelect": "en",
            "faceMatchImage": "base64image",
            "workflowPaymentCollectionConfig": {
                "amount": "500",
            },
            "gpsConfig": {
                "applyLocationRestriction": True,
                "allowedLatitude": "19.0760",
                "allowedLongitude": "72.8777",
                "permissibleRadius": 500,
                "applyLocationAccuracy": True,
                "accuracyThreshold": 100,
            },
            "aadhaarConfig": {
                "verifyName": True,
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyYob": 1990,
                "verifyTitle": "Mr",
                "verifyState": "MAHARASHTRA",
                "verifyGender": "M",
            },
            "offlineSignConfig": {
                "mobileNumber": "9876543210",
                "pan": "ABCDE1234F",
                "signerId": "SIGNER001",
                "verifyName": True,
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyState": "MAHARASHTRA",
                "verifyYob": 1990,
                "verifyTitle": "Mr",
                "verifyGender": "M",
            },
            "dscConfig": {
                "verifyName": True,
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyState": "MAHARASHTRA",
            },
            "neslConfig": {
                "verifyName": True,
                "verifySmartName": True,
                "verifyPincode": "411001",
                "verifyYob": 1990,
                "verifyTitle": "Mr",
                "verifyState": "MAHARASHTRA",
                "verifyGender": "M",
            },
        }
    ],
    "cc": [{"name": "CC User", "email": "cc@example.com"}],
    "irn": "IRN001",
}

request_model = RequestModel(**request_external_data)

print(request_model.profileId)
print(request_model.file.name)
print(request_model.neslData.documentDetail.loanNumber)
print(request_model.model_dump())
"""
{
    'profileId': '12345',
    'file': {
        'name': 'test.pdf',
        'file': 'base64encodedcontent',
        'fields': [...],
        'autoGroupedFieldsFill': True,
        'additionalFiles': None,
    },
    'stampSeries': 'SERIES001',
    'multipleStampSeries': [...],
    'seriesGroup': 'GROUP1',
    'stampValue': '500',
    'stampUpload': {...},
    'revenueStampSeries': 'REV001',
    'revenueStampQuantity': '5',
    'neslData': {...},
    'invitees': [...],
    'cc': [...],
    'irn': 'IRN001',
}
"""

response_external_data = {
    "status": 200,
    "messages": [{"code": "200", "message": "Success"}],
    "data": {
        "documentId": "DOC001",
        "irn": "IRN001",
        "invitees": [
            {
                "name": "Invitee 1",
                "email": "invitee1@example.com",
                "phone": "9876543210",
                "signUrl": "https://example.com/sign/abc123",
                "active": True,
                "expiryDate": "2024-12-31",
            }
        ],
    },
}

response_model = ResponseModel(**response_external_data)

print(response_model.status)
print(response_model.data.documentId)
print(response_model.model_dump())
"""
{
    'status': 200,
    'messages': [
        {'code': '200', 'message': 'Success'}
    ],
    'data': {
        'documentId': 'DOC001',
        'irn': 'IRN001',
        'invitees': [...],
    },
}
"""
