# ufirst API Quickstart

Aim of this document is to provide developers with all the pieces of information they need to integrate ufirst to their platform.

## Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Usage examples](#usage-examples)
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

1. (client app) The user logins on your system with her own credentials
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

### Using JWT token for Client APIs

Once you have obtained a JWT token for a given userID, you just need to execute HTTP request against ufirst APIs by adding the `authorization` header, valued as `Bearer {JWTToken}`, e.g.:

```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhmNDMyMDRhMTc5MTVlOGJlN2NjZDdjYjI2NGRmNmVhMzgzYzQ5YWIiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjEiLCJvcmlnaW5hbFVzZXJJRCI6ImFwaXYxLTEtdGVzdC11c2VyIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3FmaXJzdC10ZXN0IiwiYXVkIjoicWZpcnN0LXRlc3QiLCJhdXRoX3RpbWUiOjE2MjU0OTgwMDUsInVzZXJfaWQiOiJhcGl2MS0xLXRlc3QtdXNlciIsInN1YiI6ImFwaXYxLTEtdGVzdC11c2VyIiwiaWF0IjoxNjI1NDk4MDA1LCJleHAiOjE2MjU1MDE2MDUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.LdGktkewJpxcaA7CbxuSw3S6DQ-61R7rX5CsajwPL3tmPTV2mz6h7kLCNPNWCqjUJRft6deQxu_sFsU5h7GiwShZesE_6XmdKaXBykocwk-erwawkXDANAF36yLM81UHcWdA2A6GKiQOyqQ_9SlSf5eBlqlHoIfmuCt9jyKn3QtASobDfPVod7kmWoBcr-qJh1C61p-AMgtAKSn4xDUaAp8y-4jMXxHrVY73ji3uqHe0CZv5LzpeBhR80BINthaWiuO7qrBUhzmZE28AIt3167dtbtGv7IX4BCKdB6waQFlTSCsIcgVQkV_8yWChx7YHY43LQwNMqGJuh15aAgNKZQ
```

## Usage Examples

This chapter provides you with a brief examples to understand how to use ufirst Business APIs.

All the following examples are written in python 3, but you can choose to use the language you prefer.

### Generating a JWT token for a given user

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

You can consult the full running example [here](examples/generate_jwt_token.py)

### Reservation Issue Flow

#### List of the available points for an organization

```python
import requests

# organization_id is the unique identifier of your organization in ufirst
# systems; it is provided by ufirst when your partner account is enabled.
organization_id = '12345'

api_base_url = 'https://api.ufirst.business/v1'

# this is the JWT token retrieved from a server to server call and should never
# be hardcoded
# please refer to generate_jwt_token.py
jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnHteaY'

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

organization = response.json()
```

You can consult the full running example [here](examples/reservation_issue_flow.py)

#### List of the available services for a point

```python
import requests

#TODO
```

You can consult the full running example [here](examples/reservation_issue_flow.py)

#### Issue a reservation for a given service in a given point

```python
import requests

#TODO
```

You can consult the full running example [here](examples/reservation_issue_flow.py)

#### List all reservations issued from a given user

```python
import requests

#TODO
```

You can consult the full running example [here](examples/reservation_issue_flow.py)

#### Delete a reservation on behalf of a user

```python
import requests

#TODO
```

You can consult the full running example [here](examples/reservation_issue_flow.py)

## Webhooks

In order to avoid HTTP polling for retrieving the status of a given office and show it on a monitor (e.g. a public display which lists the reservations which are called from a given counter in an office), convenient Webhook APIs are available.

You can register a certain webhook on a given pointID so that all status updates for such point will be sent over HTTP as soon as they happen, in near realtime.

This means you need to have a machine / application which would be publicly reachable over HTTP on the Internet either via a [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) or an [IP Address](https://en.wikipedia.org/wiki/IP_address).

**NOTE**: Please note that Webhooks APIs are meant to be used in a _server to server_ environment, and they are authenticated with the `x-privatekeyid` and `x-clientemail` HTTP request headers.

**NOTE**: Only a single Webhook per pointID is allowed.
