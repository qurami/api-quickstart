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
        "headerImageURL": "https://s3.eu-central-1.amazonaws.com/files.ufirst.com/contents/organizations/1/identityHeaderImage.jpg",
        "logoURL": "https://s3.eu-central-1.amazonaws.com/files.ufirst.com/contents/organizations/1/identityLogo.png",
        "points": [
            {
                "id": "QQST000000051",
                "name": "Tutorial Office",
                "categorySlug": "services",
                "citySlug": "Rome",
                "timezone": "Europe/Rome",
                "isUfirstBusiness": false,
                "businessDays": [
                    {
                        "weekday": 0,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    },
                    {
                        "weekday": 1,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    },
                    {
                        "weekday": 2,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "1859"
                    },
                    {
                        "weekday": 5,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    },
                    {
                        "weekday": 6,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    },
                    {
                        "weekday": 3,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    },
                    {
                        "weekday": 4,
                        "startTimeISO8601": "0000",
                        "endTimeISO8601": "2359"
                    }
                ]
            }
        ]
    }

    '''
    print(organization)


def get_point_services():
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    # point_id is the identifier of the Point for which we want to obtain
    # the list of available services.
    point_id = 'QQSP000000100'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnGteaY'

    organization_url = "%s/organizations/%s/points/%s" % (
        api_base_url,
        organization_id,
        point_id
    )

    headers = {
        'authorization': "Bearer %s" % jwt_token_for_user,
    }

    response = requests.get(
        url=organization_url,
        headers=headers,
    )

    point = response.json()

    '''
    should print the struct of the point with its available services, e.g.

    {
      "id": "QQSP000000100",
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
          "id": "QQSP000000100-demo-service",
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
          "isScheduled": true,
          "durationInMinutes": 20,
          "peopleInLine": 7
        }
      ]
    }

    '''
    print(point)


# example parameters:
# service_id: 'QQSP000000100-demo-service'
# payload:
# {
#   "reservationParametersValues": [
#        {
#            "reservationParameterID": "name",
#            "reservationParameterValue": "ilMioNome"
#        },
#        {
#            "reservationParameterID": "phone-number",
#            "reservationParameterValue": "000000000"
#        }
#    ],
# }
def issue_reservation_for_service(service_id: str, parameters: object):
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    # point_id is the identifier of the Point for which we want to obtain
    # the list of available services.
    point_id = 'QQSP000000100'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnGteaY'

    organization_url = "%s/organizations/%s/points/%s/services/%s/reservations" % (
        api_base_url,
        organization_id,
        point_id,
        service_id
    )

    headers = {
        'authorization': "Bearer %s" % jwt_token_for_user,
    }

    response = requests.post(
        url=organization_url,
        json=parameters,
        headers=headers,
    )

    point = response.json()

    '''
    should print the struct of the newly created reservation, e.g.

    {
      "id": "5df2451835ac1e465abd948c",
      "label": "C22",
      "createdAtRFC3339": "2021-05-19T09:52:59.102-06:00",
      "pointID": "QQSP000000100",
      "serviceID": "QQSP000000100-demo-service",
      "serviceName": "Demo service",
      "state": "waiting",
      "userID": "Xxdvk4m0y5WJWoKtM12R7vCojXo2",
      "scheduledServingTimeRFC3339": "2021-05-20T00:00:00-06:00",
      "peopleAhead": 10,
      "estimatedServingTimeRFC3339": "2021-05-20T00:00:00-06:00"
    }
    
    '''
    print(point)


# get_issued_reservations prints all the previously issued reservations
# for the given user_id.
def get_issued_reservations(user_id: str):
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnGteaY'

    organization_url = "%s/organizations/%s/users/%s/reservations" % (
        api_base_url,
        organization_id,
        user_id
    )

    headers = {
        'authorization': "Bearer %s" % jwt_token_for_user,
    }

    response = requests.get(
        url=organization_url,
        headers=headers,
    )

    point = response.json()

    '''
    should print the list of the previously issued reservation for the given user_id, e.g.

    [
      {
        "id": "5df2451835ac1e465abd948c",
        "label": "C22",
        "createdAtRFC3339": "2021-05-19T09:52:59.102-06:00",
        "pointID": "QQSP000000100",
        "serviceID": "QQSP000000100-demo-service",
        "serviceName": "Demo service",
        "state": "waiting",
        "userID": "Xxdvk4m0y5WJWoKtM12R7vCojXo2",
        "scheduledServingTimeRFC3339": "2021-05-20T00:00:00-06:00",
        "peopleAhead": 10,
        "estimatedServingTimeRFC3339": "2021-05-20T00:00:00-06:00"
      }
    ]

    '''
    print(point)


# get_issued_reservations prints all the previously issued reservations
# for the given user_id.
def delete_reservation(user_id: str, reservation_id: str):
    # organization_id is the unique identifier of your organization in ufirst
    # systems; it is provided by ufirst when your partner account is enabled.
    organization_id = '12345'

    api_base_url = 'https://api.ufirst.business/v1'

    # this is the JWT token retrieved from a server to server call
    # please refer to generate_jwt_token.py
    jwt_token_for_user = 'eyJhbGciOiJSUzI1NiIsImtpXCI6IjhiMjFkNWE1Y2U2OGM1MjNlZTc0MzI5YjQ3ZDg0NGE3YmZjODRjZmYiLCJ0eXAiOiJKV1QifQ.eyJvcmdhbml6YXRpb25JRCI6IjI1Iiwib3JpZ2luYWxVc2VySUQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdWQiOiJhcGktcHJvamVjdC03MDI2OTI3MDI1MTkiLCJhdXRoX3RpbWUiOjE2MjU1MDE3ODYsInVzZXJfaWQiOiJhcGl2MS0yNS1qb24uYXBwbGVzZWVkQHlvdXJjb21wYW55Lm9yZyIsInN1YiI6ImFwaXYxLTI1LWpvbi5hcHBsZXNlZWRAeW91cmNvbXBhbnkub3JnIiwiaWF0IjoxNjI1NTAxNzg2LCJleHAiOjE2MjU1MDUzODYsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.d2K7n105d1ZmbaM7677gcBkZWiNIAtyuheNAliNl2oK9SJVDTQzaGDjgkbQVH1bOCypiVFmAxOIMVbJchrLs6QqwcAsEC9zXulNJQDPGzbfYpVc53_tH8SyXCu_XJXHwuter9bZA0lYnLQoMpFRd4Y4E2wZQoLK_lvTUElUfEDSgzgp-wiAVEKbTCGrbOmUqBkwT3xzHcmIvJDOE07V_AVMwLd3au7n5esvDNOt1mX797CVPpgh9bCRJnaXj1vIGGYe6agTjsvAyy9onEUrQDS5H-h2bx5finQAb_yOj_-gVnA9TnFRLVfy9OabR0b-CO3agM6ks9zRQTLunnGteaY'

    organization_url = "%s/organizations/%s/users/%s/reservations/%s" % (
        api_base_url,
        organization_id,
        user_id,
        reservation_id
    )

    headers = {
        'authorization': "Bearer %s" % jwt_token_for_user,
    }

    response = requests.delete(
        url=organization_url,
        headers=headers,
    )

    point = response.json()

    '''
    should print the response status code, should be 204 in case of success.
    '''
    print(response.status_code)


if __name__ == '__main__':
    get_organization()

    get_point_services()

    service_id = 'QQSP000000100-demo-service'
    parameters = {
      "reservationParametersValues": [
           {
               "reservationParameterID": "name",
               "reservationParameterValue": "ilMioNome"
           },
           {
               "reservationParameterID": "phone-number",
               "reservationParameterValue": "000000000"
           }
       ],
    }
    issue_reservation_for_service(service_id=service_id, parameters=parameters)

    user_id = 'jon.appleseed@yourcompany.org'
    get_issued_reservations(user_id=user_id)

    reservation_id = '5df2451835ac1e465abd948c'
    delete_reservation(user_id=user_id, reservation_id=reservation_id)