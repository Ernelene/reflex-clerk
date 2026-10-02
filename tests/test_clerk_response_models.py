import pytest

from custom_components.reflex_clerk.clerk_client.clerk_response_models import (
    User,
    Verification,
)


@pytest.mark.parametrize(
    "strategy",
    [
        "ticket",
        "oauth_google",
        "oauth_github",
        "oauth_mock",
        "admin",
        "phone_code",
        "email_code",
        "reset_password_email_code",
        "web3_metamask_signature",
        "from_oauth_google",
        "from_oauth_github",
    ],
)
def test_verification_accepts_clerk_strategies(strategy):
    verification = Verification(strategy=strategy, status="verified")

    assert verification.strategy == strategy


@pytest.mark.parametrize("payload", [{}, {"strategy": None}])
def test_verification_accepts_missing_or_null_strategy(payload):
    verification = Verification(**payload)

    assert verification.strategy is None


def test_user_created_through_organization_invitation_parses():
    payload = {
        "id": "user_2abc123",
        "object": "user",
        "external_id": None,
        "primary_email_address_id": "idn_2abc123",
        "primary_phone_number_id": None,
        "primary_web3_wallet_id": None,
        "username": None,
        "first_name": "Ada",
        "last_name": "Lovelace",
        "profile_image_url": "https://img.clerk.com/example",
        "image_url": "https://img.clerk.com/example",
        "has_image": False,
        "public_metadata": {},
        "private_metadata": {},
        "unsafe_metadata": {},
        "email_addresses": [
            {
                "id": "idn_2abc123",
                "object": "email_address",
                "email_address": "ada@example.com",
                "reserved": False,
                "verification": {"strategy": "ticket"},
                "linked_to": [],
                "created_at": 1_725_000_000_000,
                "updated_at": 1_725_000_000_000,
            }
        ],
        "phone_numbers": [],
        "web3_wallets": [],
        "passkeys": [],
        "saml_accounts": [],
        "password_enabled": False,
        "two_factor_enabled": False,
        "totp_enabled": False,
        "backup_code_enabled": False,
        "last_sign_in_at": None,
        "banned": False,
        "locked": False,
        "created_at": 1_725_000_000_000,
        "updated_at": 1_725_000_000_000,
        "last_active_at": 1_725_000_000_000,
        "create_organization_enabled": True,
        "create_organizations_limit": None,
        "delete_self_enabled": True,
        "legal_accepted_at": None,
    }

    user = User(**payload)

    assert user.email_addresses[0].verification.strategy == "ticket"
