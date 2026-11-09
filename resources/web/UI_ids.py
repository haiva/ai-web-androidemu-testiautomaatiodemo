"""Lokaattorit: yle.fi (työpöytäselain), Browser Library.

Arvot, joissa on 'TODO', vahvistetaan RF-MCP:llä (/tutki-web).
Yle Tunnus -kirjautuminen avautuu dialogiin, jonka sisältö on tunnus.yle.fi-iframessa;
Browser läpäisee iframen '>>>'-erottimella.
"""

# --- Evästeet ---
COOKIE_CONSENT_REJECT_BUTTON = '#yle-consent-sdk-container >> role=button[name="Vain välttämättömät"]'

# --- Kirjautuminen (Yle Tunnus) ---
LOGIN_ENTRY_BUTTON = '[data-testid="header-login-button"]'
LOGIN_DIALOG = '[data-testid="tunnus-sdk-dialog"]'
LOGIN_EMAIL_INPUT = '#tunnus-sdk__content >>> #emailAddress'
LOGIN_PASSWORD_INPUT = '#tunnus-sdk__content >>> [data-testid="password-input"]'
LOGIN_SUBMIT_BUTTON = '#tunnus-sdk__content >>> role=button[name="Kirjaudu sisään"]'
LOGGED_IN_INDICATOR = '[data-testid="header-user-menu-toggle"]'   # nimikirjaimet, näkyy vain kirjautuneena
USER_MENU_TOGGLE = '[data-testid="header-user-menu-toggle"]'
LOGOUT_BUTTON = '[data-testid="header-logout-button"]'            # piilossa, kunnes USER_MENU_TOGGLE avattu

# --- Navigaatio (pää- ja alaprofiili) ---
# TODO: yläpalkin osiot, esim. Uutiset, Urheilu
MAIN_ACCOUNT_NAVIGATION_ITEMS = ["TODO"]
SUB_ACCOUNT_NAVIGATION_ITEMS = ["TODO"]
