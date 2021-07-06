# -*- coding: utf-8 -*-

import requests


def read_webhooks():
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


def create_webhook():
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


def update_webhook():
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


def delete_webhook():
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


if __name__ == '__main__':
    read_webhooks()
    create_webhook()
    update_webhook()
    delete_webhook()
