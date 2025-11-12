import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 31465200
API_HASH = "e60f89caed7d2861ecddf0e5c54159b5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8595644382:AAGMUM7G4OAQtdQ7ubVy4YjzTOiZuMqYe2k"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://crazyjaatabhi_86: crazyjaatabhi_86@crazyjaatabhi.wbikzkk.mongodb.net/?appName=crazyjaatabhi"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1003354979541

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8438029944

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/qtkitten_86"
SUPPORT_GROUP = "https://t.me/qtkitten_86"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQHgHvAAC7YZpSIeTNizFzpV5nzR2O7b6hJ02Cf5ErqCqnI6_8hIHCHEiqUGLNmrJ1uvB-J2oaZudT8HjGKZIi4J43QI5lePe4BcGPI7T_2Tpqe284Kv9Igh13N6sAjsEJbhUh7vI7r3BBsyoCpynMeYf20ZE-Hhb1X4kQWzBHSV87ZApBVg8Hirl_n_wJZrLyybqczGQaUydUdyV6hTVqkvDAsXjc3m_K2LzIvMJuqkpkwX6-1s2Us-0GWfhT_ViCvX1X8je8IG69PgRwLZq99kJAOcpgvV09paFHsP9nClDLZRHKaOvjHqN1aDkTOs4eFl4-91Vy2HnbmOwNAVjD8vuLwHKwAAAAH28h54AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"

PING_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
STATS_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
STREAM_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/da71394f631b699fcb9d3-55283d87c41550c9dc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

