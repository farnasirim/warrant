class WarrantException(Exception):
    """Base class for all Warrant exceptions"""


class ForceChangePasswordException(WarrantException):
    """Raised when the user is forced to change their password"""


class TokenVerificationException(WarrantException):
    """Raised when token verification fails."""

class ProvideMFATokenAction(WarrantException):
    """Raised when mfa code is required to continue the auth flow"""
    def __init__(self, context, callback):
        self.context = context
        self.callback = callback

    def provide_mfa_code(self, mfa_code):
        self.context["SOFTWARE_TOKEN_MFA_CODE"] = mfa_code
        return self.callback(context=self.context)
