import os


class Config:

BOT_TOKEN = "5389147124:AAEjGJrJWgW41pk2pexeric1Qr77CzR13MM"

    API_ID = "14219833"

    API_HASH = "3889273685fafce5e76d76a2ad6b00e8"

    CLIENT_ID = "61391530394-vp359e09g0begugu89i5r9majo05mduo.apps.googleusercontent.com"

    CLIENT_SECRET = "972494475103-89vbfu8oa6h93esviv974v10md2eejfe.apps.googleusercontent.com"

    BOT_OWNER = "624259152"

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 624259152] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
