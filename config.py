#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5757059757:AAEvjvpv1gmn8xHGAONAiTEjEbN7OaHwka8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9844066"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQDBpE0ZPemEfT-BSYzl6fems8x5ghVgO8IpOCPRjBR4F-egaX4rv38hB6MXa3Neoa_6QRCVLjmeOo-iRA_VRDv_iwjiPNp1YD662eZO7HTEv2MinEz891ilmjk7zy5dT1iwv65S4i_zzShfugHRkgnFrqHvn0tcdwwn7AngARpaRUWbzIU2ry0Fiy7msIP5PZCrXdkZc4UeAV4EAjYVlMdj9W6oOTizcm4PNvAsbehHRNbq1gx-SwcnRP92svxeK497fsWLYaC6u0nYTACmVXRlEw_bTVruRs_7QwEuWLWWGsHSUzfvbCfFZgkDcpkXlZEsoGNPNsnDSt83EEiyBAxtaYcCeAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a.oregon-postgres.render.com/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
