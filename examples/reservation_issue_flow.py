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


if __name__ == '__main__':
    get_organization()
