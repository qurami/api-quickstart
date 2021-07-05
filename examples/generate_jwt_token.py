# -*- coding: utf-8 -*-

import requests


def main():
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


if __name__ == '__main__':
    main()
