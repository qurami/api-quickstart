# ufirst API QuickStart

The aim of this document is to provide developers with all the pieces of information they need to integrate ufirst to their platform.

## Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Reservation Flow](#reservation-flow)
- [Webhooks](#webhooks)

## Overview

ufirst Business APIs provide partners with the ability to integrate the entire lifecycle of reservations on their own application using ufirst as the backend. They can be used to programmatically get the status of a given point and issue reservations on behalf of a user.

To get access to the ufirst API you must first apply for a partner account and have your use case approved.

ufirst APIs are based on the [REST Protocol](http://en.wikipedia.org/wiki/Representational_State_Transfer) with predictable resource-oriented URLs, form-encoded request bodies and JSON-encoded responses.

The list of the available APIs, the exchanged models, can be accessed at [http://docs.api.ufirst.business/](http://docs.api.ufirst.business/).

## Authentication

All requests to ufirst APIs must be authenticated.

As you will see, some APIs are exclusively meant to be used in a _server to server_ environment, as they are authenticated via your organization's credentials which MUST NOT be shared with 3rd-party clients.

On the other hand, the APIs designed around the reservation lifecycle are authorized via a [JWT token](https://jwt.io/), which is generated on behalf of a specific user within your organization and can be consumed directly from a client application.

The authentication flow can be represented as follows:

1. (client app) The user logins on your backend with her own credentials
2. (client app) Calls your backend to retrieve a JWT token to access ufirst APIs
3. (your backend) Executes a request to ufirst APIs with your organization's credentials to issue a JWT token on behalf on the specific user
4. (ufirst API) Returns a JWT token to your backend
5. (your backend) Returns the token to the client app
6. (client app) Executes an API call to ufirst API using the provided JWT token

**NOTE**: Please bear in mind that all JWT tokens expire 60 minutes after the time of their creation.

### Generating a JWT token on behalf of a user

Execute a `POST` request to `https://api.ufirst.business/v1/organizations/{organizationID}/users/{userID}/login`, where:

- {organizationID} is the unique identifier of your organization we provided,
- {userID} is the unique identifier of your user within your organization; it can be a username, an email, the unique user identifier in your database, the ID/number of the loyalty card, etc.

You also need to send the following [HTTP Headers](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_header_fields) using the values we provided you once your partner account has been enabled:

- `x-privatekeyid`
- `x-clientemail`

The return payload is a string representing the JWT token.

**NOTE**: Please bear in mind that the returned JWT token will identify the specific userID you have provided; such JWT token SHALL NOT be used across multiple/different users!

#### Usage Example

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# provided by ufirst when your partner account is enabled.
private_key_id = 'you-private-key-id'

# provided by ufirst when your partner account is enabled.
client_email_address = 'your-private-email-address@api-project-702692702519.iam.gserviceaccount.com'

# this represents the user identifier which you are generating the token
# on behalf of; remember that it should not be hardcoded as this example!
user_id = 'jon.appleseed@yourcompany.org'

api_base_url = 'https://api.ufirst.business/v1'

generate_jwt_token_for_user_url = "%s/organizations/%s/users/%s/login" % (
    api_base_url,
    organization_id,
    user_id,
)

server_to_server_auth_headers = {
    'x-privatekeyid': private_key_id,
    'x-clientemail': client_email_address,
}

response = requests.post(
    url=generate_jwt_token_for_user_url,
    headers=server_to_server_auth_headers,
)

jwt_token_for_user = response.json()

# should print the JWT token, e.g.
# eyJhbGciOiJSUzI1NiIsImtpZCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE... [omitted]
print(jwt_token_for_user)
```

### Using JWT token for Client APIs

Once you have obtained a JWT token for a given userID, you just need to execute HTTP request against ufirst APIs by adding the `authorization` header, valued as `Bearer {JWTToken}`.

## Reservation Flow

![Reservation Flow Scheme](./assets/reservation-flow.svg)

### List of the available points for an organization

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call and should never
# be hardcoded
# please refer to generate_jwt_token.py
jwt_token_for_user = 'your.generated.jwttoken'

organization_url = "%s/organizations/%s" % (
    api_base_url,
    organization_id,
)

headers = {
    'authorization': "Bearer %s" % jwt_token_for_user,
}

response = requests.get(
    url=organization_url,
    headers=headers,
)

'''
should print the struct of the organization with its active points, e.g.

{
    "id": "1",
    "name": "ufirst",
    "fullName": "ufirst",
    "headerImageURL": "https://example.com/header.png",
    "logoURL": "https://example.com/logo.png",
    "points": [
        {
            "id": "QQSP123456789",
            "name": "Demo point",
            "categorySlug": "health",
            "citySlug": "rome",
            "timezone": "Europe/Rome",
            "isUfirstBusiness": true,
            "businessDays": [
                {
                    "weekday": 1,
                    "startTimeISO8601": "1000",
                    "endTimeISO8601": "1230"
                }
            ]
        }
    ]
}

'''
organization_with_points = response.json()
print(organization_with_points)
```

### List of the available services for a point

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# point_id is the identifier of the Point for which we want to obtain
# the list of available services.
point_id = 'QQSP123456789'

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call
# please refer to generate_jwt_token.py
jwt_token_for_user = 'your.generated.jwttoken'

point_with_services_url = "%s/organizations/%s/points/%s" % (
    api_base_url,
    organization_id,
    point_id
)

headers = {
    'authorization': "Bearer %s" % jwt_token_for_user,
}

response = requests.get(
    url=point_with_services_url,
    headers=headers,
)

'''
should print the struct of the point with its available services and other relevant information, e.g.

{
    "id": "QQSP123456789",
    "name": "Demo point",
    "categorySlug": "health",
    "geoPoint": {
        "latitude": 41.902,
        "longitude": 12.501,
        "name": "Via Giovanni Amendola 46, 00185 Roma Italia"
    },
    "countrySlug": "italy",
    "citySlug": "rome",
    "timezone": "Europe/Rome",
    "isUfirstBusiness": true,
    "businessDays": [
        {
            "weekday": 1,
            "startTimeISO8601": "1000",
            "endTimeISO8601": "1230"
        }
    ],
    "organization": {
        "id": "1",
        "name": "ufirst",
        "fullName": "ufirst",
        "headerImageURL": "https://example.com/header.png",
        "logoURL": "https://example.com/logo.png"
    },
    "services": [
        {
            "id": "QQSP123456789-demo-service",
            "name": "Demo service",
            "reservationParameters": [
                {
                    "id": "contact-phone-number",
                    "label": "Your phone number",
                    "placeholder": "1234567890",
                    "regex": "^[0-9]{9,40}$|^none$",
                    "resourcesAvailability": []
                },
                {
                    "id": "timeslot",
                    "label": "Select the day and hour for the service",
                    "placeholder": "",
                    "regex": "",
                    "resourcesAvailability": [
                        {
                            "resourceID": "123456789-T_resource",
                            "resourceName": "Entrance",
                            "timeslots": [
                                {
                                    "startTimeISO8601": "1000",
                                    "maxPartySize": 100
                                },
                                {
                                    "startTimeISO8601": "1100",
                                    "maxPartySize": 100
                                },
                                {
                                    "startTimeISO8601": "1200",
                                    "maxPartySize": 100
                                }
                            ]
                        }
                    ]
                }
            ],
            "isActive": true,
            "isScheduled": true
        }
    ]
}

'''
point_with_services = response.json()
print(point_with_services)
```

### Issue a reservation for a given service in a given point

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# point_id is the identifier of the Point for which we want to obtain
# the list of available services.
point_id = 'QQSP123456789'

# service_id is the identifier of the service we want to issue a
# reservation for.
service_id = 'QQSP123456789-demo-service'

# parameters is the request payload with the reservation parameters.
parameters = {
    "reservationParametersValues": [
        {
            "reservationParameterID": "contact-phone-number",
            "reservationParameterValue": "000000000"
        },
        {
            "reservationParameterID": "timeslot",
            "selectedAvailability": {
              "resourceID": "123456789-T_resource",
              "timeslotStartTimeRFC3339": "2021-06-05T11:00:00+01:00"
            }
        }
    ],
}

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call
# please refer to generate_jwt_token.py
jwt_token_for_user = 'your.generated.jwttoken'

issue_reservation_url = "%s/organizations/%s/points/%s/services/%s/reservations" % (
    api_base_url,
    organization_id,
    point_id,
    service_id
)

headers = {
    'authorization': "Bearer %s" % jwt_token_for_user,
}

response = requests.post(
    url=issue_reservation_url,
    json=parameters,
    headers=headers,
)

'''
should print the struct of the newly created reservation, e.g.

{
    "id": "5df2451835ac1e465abd948c",
    "label": "C22",
    "createdAtRFC3339": "2021-05-19T09:52:59.102-06:00",
    "pointID": "QQSP123456789",
    "serviceID": "QQSP123456789-demo-service",
    "serviceName": "Demo service",
    "state": "waiting",
    "userID": "jon.appleseed@yourcompany.org",
    "scheduledServingTimeRFC3339": "2021-06-05T11:00:00+01:00"
}

'''
reservation = response.json()
print(reservation)
```

### Delete a reservation on behalf of a user

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# this represents the user identifier.
user_id = 'jon.appleseed@yourcompany.org'

# reservation_id is the identifier of the reservation we intend to delete.
reservation_id = '5df2451835ac1e465abd948c'

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call
# please refer to generate_jwt_token.py
jwt_token_for_user = 'your.generated.jwttoken'

delete_reservation_url = "%s/organizations/%s/users/%s/reservations/%s" % (
    api_base_url,
    organization_id,
    user_id,
    reservation_id
)

headers = {
    'authorization': "Bearer %s" % jwt_token_for_user,
}

response = requests.delete(
    url=delete_reservation_url,
    headers=headers,
)

print(response.status_code)
```

### List all reservations issued from a given user

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# this represents the user identifier.
user_id = 'jon.appleseed@yourcompany.org'

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call
# please refer to generate_jwt_token.py
jwt_token_for_user = 'your.generated.jwttoken'

reservations_url = "%s/organizations/%s/users/%s/reservations" % (
    api_base_url,
    organization_id,
    user_id
)

headers = {
    'authorization': "Bearer %s" % jwt_token_for_user,
}

response = requests.get(
    url=reservations_url,
    headers=headers,
)

'''
should print the list of the previously issued reservation for the given user_id, e.g.

[
    {
        "id": "5df2451835ac1e465abd948c",
        "label": "C22",
        "createdAtRFC3339": "2021-05-19T09:52:59.102-06:00",
        "pointID": "QQSP123456789",
        "serviceID": "QQSP123456789-demo-service",
        "serviceName": "Demo service",
        "state": "waiting",
        "userID": "jon.appleseed@yourcompany.org",
        "scheduledServingTimeRFC3339": "2021-06-05T11:00:00+01:00"
    }
]

'''
reservation_list = response.json()
print(reservation_list)
```

## Webhooks

In order to obtain real time updates regarding the status of a given office and show it on a monitor (e.g. a public display which lists the reservations which are called from a given counter in an office), convenient Webhook APIs are available.

You can register a certain webhook on a given pointID so that all status updates for such point will be sent over HTTP as soon as they happen, in near realtime.

This means you need to have a machine / application which would be publicly reachable over HTTP on the Internet either via a [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) or an [IP Address](https://en.wikipedia.org/wiki/IP_address).

**NOTE**: Please note that Webhooks APIs are meant to be used in a _server to server_ environment as they are authenticated with the `x-privatekeyid` and `x-clientemail` HTTP request headers.

**NOTE**: Only a single Webhook per pointID is allowed.

### List the active Webhooks for a given pointID

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# provided by ufirst when your partner account is enabled.
private_key_id = 'you-private-key-id'

# provided by ufirst when your partner account is enabled.
client_email_address = 'your-private-email-address@api-project-702692702519.iam.gserviceaccount.com'

# ufirst unique identifier of the pointID you want to activate a webhook for.
point_id = 'QQSP123456789'

api_base_url = 'https://api.ufirst.business/v1'

read_webhooks_url = "%s/organizations/%s/points/%s/webhooks" % (
    api_base_url,
    organization_id,
    point_id,
)

server_to_server_auth_headers = {
    'x-privatekeyid': private_key_id,
    'x-clientemail': client_email_address,
}

response = requests.get(
    url=read_webhooks_url,
    headers=server_to_server_auth_headers,
)

webhooks = response.json()

'''
should print the list of active webhooks for that pointID

[
    {
        "id": "60d5b56d51bb0a80f3aa34d2",
        "target": "resourcesWithReservations",
        "url": "https://my.example.domain/webhook"
    }
]
'''
print(webhooks)
```

### Create a new Webhook for a given pointID

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# provided by ufirst when your partner account is enabled.
private_key_id = 'you-private-key-id'

# provided by ufirst when your partner account is enabled.
client_email_address = 'your-private-email-address@api-project-702692702519.iam.gserviceaccount.com'

# ufirst unique identifier of the pointID you want to activate a webhook for.
point_id = 'QQSP123456789'

api_base_url = 'https://api.ufirst.business/v1'

create_webhook_url = "%s/organizations/%s/points/%s/webhooks" % (
    api_base_url,
    organization_id,
    point_id,
)

server_to_server_auth_headers = {
    'x-privatekeyid': private_key_id,
    'x-clientemail': client_email_address,
}

request_payload = {
    # please consult docs.api.ufirst.business for available targets
    'target': 'resourcesWithReservations',
    'url': 'https://url.to/another/webhook',
}

response = requests.post(
    url=create_webhook_url,
    headers=server_to_server_auth_headers,
    json=request_payload,
)

'''
should print the just created webhook,
if there's no error nor conflict

{
    "id": "60d5b56d51bb0a80f3aa34d2",
    "target": "resourcesWithReservations",
    "url": "https://url.to/another/webhook"
}
'''
new_webhook = response.json()
print(new_webhook)
```

### Edit an existing Webhook

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# provided by ufirst when your partner account is enabled.
private_key_id = 'you-private-key-id'

# provided by ufirst when your partner account is enabled.
client_email_address = 'your-private-email-address@api-project-702692702519.iam.gserviceaccount.com'

# ufirst unique identifier of the pointID you want to activate a webhook for.
point_id = 'QQSP123456789'

# ufirst unique identifier of the webhook you want to update.
webhook_id = '60e42ae973b91c55c7018a04'

api_base_url = 'https://api.ufirst.business/v1'

update_webhook_url = "%s/organizations/%s/points/%s/webhooks/%s" % (
    api_base_url,
    organization_id,
    point_id,
    webhook_id,
)

server_to_server_auth_headers = {
    'x-privatekeyid': private_key_id,
    'x-clientemail': client_email_address,
}

request_payload = {
    # please consult docs.api.ufirst.business for available targets
    'target': 'resourcesWithReservations',
    'url': 'https://this.is.a.new/webhook/url',
}

response = requests.put(
    url=update_webhook_url,
    headers=server_to_server_auth_headers,
    json=request_payload,
)

'''
should print the updated webhook,
if there's no error nor conflict

{
    "id": "60d5b56d51bb0a80f3aa34d2",
    "target": "resourcesWithReservations",
    "url": "https://this.is.a.new/webhook/url"
}
'''
updated_webhook = response.json()
print(updated_webhook)
```

### Deleting an existing Webhook

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

# provided by ufirst when your partner account is enabled.
private_key_id = 'you-private-key-id'

# provided by ufirst when your partner account is enabled.
client_email_address = 'your-private-email-address@api-project-702692702519.iam.gserviceaccount.com'

# ufirst unique identifier of the pointID you want to activate a webhook for.
point_id = 'QQSP123456789'

# ufirst unique identifier of the webhook you want to delete.
webhook_id = '60e42ae973b91c55c7018a04'

api_base_url = 'https://api.ufirst.business/v1'

delete_webhook_url = "%s/organizations/%s/points/%s/webhooks/%s" % (
    api_base_url,
    organization_id,
    point_id,
    webhook_id,
)

server_to_server_auth_headers = {
    'x-privatekeyid': private_key_id,
    'x-clientemail': client_email_address,
}

response = requests.delete(
    url=delete_webhook_url,
    headers=server_to_server_auth_headers,
)

# in that case the response will be empty
# and the response status code for a successful deletion
# should be 204
```
