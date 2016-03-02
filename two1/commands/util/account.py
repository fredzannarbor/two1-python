"""Utility functions for user accounts."""
# standard python imports
import sys

# 3rd party imports
import click

# two1 imports
import two1
from two1.commands.util import uxstring
from two1.commands import login


def get_or_create_username(config, machine_auth):
    """ Gets an existing username or creates a new account

        On a bitcoin computer a user can create one account per
        machine auth wallet. When not on a BC a user must log into
        an existing account created at the free signup page.

    Args:
        config (Config): config object used for getting .two1 information
        machine_auth (MachineAuthWallet): machine auth wallet used for authentication

    Returns:
        str: username of the current user on the system
    """
    # User hasn't logged in with the wallet
    if not config.mining_auth_pubkey:
        # A user can create an account on a BC
        if two1.TWO1_DEVICE_ID:
            login.create_account_on_bc(config, machine_auth)

        # log into an existing account
        else:
            login.login_account(config, machine_auth)

    if not config.username:
        click.echo(uxstring.UxString.Error.login_error_username)
        sys.exit(1)

    if not config.mining_auth_pubkey:
        click.echo(uxstring.UxString.Error.login_error_mining_auth_pubkey)
        sys.exit(2)

    return config.username

