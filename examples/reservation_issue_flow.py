# -*- coding: utf-8 -*-

import requests


def get_organization():
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnGteaY'

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
    print(organization)


def get_point_with_services():
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    # point_id is the identifier of the Point for which we want to obtain
    # the list of available services.
    point_id = 'QQSP123456789'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.fyGvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3ZzdH9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRSTLunnGteaY'

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

    point_with_services = response.json()

    '''
    should print the struct of the point with its available services, e.g.

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
                        "id": "phone-number",
                        "label": "Your phone number",
                        "placeholder": "1234567890",
                        "regex": "^[0-9]{9,40}$|^none$",
                        "resourcesAvailability": [
                            {
                                "resourceID": "100-S_demo-resource",
                                "resourceName": "Demo resource",
                                "timeslots": [
                                    {
                                        "startTimeRFC3339": "2021-06-05T19:13:00+01:00",
                                        "maxPartySize": 10
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
    print(point_with_services)


def issue_reservation_for_service():
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
                "reservationParameterID": "name",
                "reservationParameterValue": "myFullName"
            },
            {
                "reservationParameterID": "phone-number",
                "reservationParameterValue": "000000000"
            }
        ],
    }

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.fyGvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3ZzdH9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRSTLunnGteaY'

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
      "userID": "Xxdvk4m0y5WJWoKtM12R7vCojXo2",
      "scheduledServingTimeRFC3339": "2021-05-20T00:00:00-06:00",
      "peopleAhead": 10,
      "estimatedServingTimeRFC3339": "2021-05-20T00:00:00-06:00"
    }
    
    '''
    reservation = response.json()
    print(reservation)


def get_issued_reservations():
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    # this represents the user identifier.
    user_id = 'jon.appleseed@yourcompany.org'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.fyGvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3ZzdH9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRSTLunnGteaY'

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
        "userID": "Xxdvk4m0y5WJWoKtM12R7vCojXo2",
        "scheduledServingTimeRFC3339": "2021-05-20T00:00:00-06:00",
        "peopleAhead": 10,
        "estimatedServingTimeRFC3339": "2021-05-20T00:00:00-06:00"
      }
    ]

    '''
    reservation_list = response.json()
    print(reservation_list)


def delete_reservation():
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
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.fyGvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3ZzdH9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRSTLunnGteaY'

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

    '''
    should print the response status code, 204 in case of success.
    '''
    print(response.status_code)


if __name__ == '__main__':
    get_organization()
    get_point_with_services()
    issue_reservation_for_service()
    get_issued_reservations()
    delete_reservation()
