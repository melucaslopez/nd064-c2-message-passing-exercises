## Request to order a computer
REQUEST:
    "HTTP method": POST
    "URL": <BASE_URL>/api/orders/computers
    "headers": Content-Type: application/json
    "request_body": {
        "created_by": <user_id: str>,
        "status": <status_enum: str>,
        "created_at": <isoformat_timestamp: str>,
        "equipment": [<equipment: str>]
    }

RESPONSE:
    "response_code": 201
    "headers": Accept: application/json
    "response_body": {
        "created_by": <user_id: str>,
        "status": <status_enum: str>,
        "created_at": <isoformat_timestamp: str>,
        "equipment": [<equipment: str>]
    }

## Request to retrieve orders
REQUEST:
    "HTTP method": GET
    "URL": <BASE_URL>/api/orders/computers

RESPONSE:
    "response_code": 200
    "headers": Accept: application/json
    "response_body": {
        "computer_orders": [
            {
                "created_by": <user_id: str>,
                "status": <status_enum: str>,
                "created_at": <isoformat_timestamp: str>,
                "equipment": [<equipment: str>]
            }
        ]
    }

## Alternative request for general order
REQUEST:
    "HTTP method": POST
    "URL": <BASE_URL>/api/orders/computers
    "headers": Content-Type: application/json
    "request_body": {
        "created_by": <user_id: str>,
        "status": <status_enum: str>,
        "created_at": <isoformat_timestamp: str>,
        "details": {
            "type": <type_enum: str>,
            "equipment": [<equipment: str>]
        }
    }

RESPONSE:
    "response_code": 201
    "headers": Accept: application/json
    "response_body": {
        "created_by": <user_id: str>,
        "status": <status_enum: str>,
        "created_at": <isoformat_timestamp: str>,
        "details": {
            "type": <type_enum: str>,
            "equipment": [<equipment: str>]
        }
    }