#XO-N0VA
import re
from os import environ
from Script import *

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '14505719'))
API_HASH = environ.get('API_HASH', '620f0a2aa2cd1474a4953619b3e3643d')
BOT_TOKEN = environ.get('BOT_TOKEN', '7349715068:AAEFFwlLuRWih8-L-l9O9MC1l1L41aiLoNk')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/ea52f1f3525a6d914347f.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/ea52f1f3525a6d914347f.jpg")
TUTORIAL_VIDEO = environ.get("TUTORIAL_VIDEO", "")
MELCOW_VID = environ.get("MELCOW_VID", "")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/28dbfb94b3b6e5540ccb1.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1652683874').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002094774771')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', "-1001852649500")
reqst_channel = environ.get('REQST_CHANNEL_ID', "-1002103699846")
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), True)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Prosearchbot:Prosearchbot@cluster0.21sz0bo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "rmies")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'rxmov_files')

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "0")
VERIFY2_URL = environ.get('VERIFY2_URL', "tnshort.net")
VERIFY2_API = environ.get('VERIFY2_API', "b6aace46d40c605fff8e0cafbcd8fbe416851f4d")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnshort.net')
SHORTLINK_API = environ.get('SHORTLINK_API', 'b6aace46d40c605fff8e0cafbcd8fbe416851f4d')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/movies4u26')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/movies4uu2')
MSG_ALRT = environ.get('MSG_ALRT', 'ᴠᴀʟᴀʀ ᴍᴏʀɢʜᴜʟɪs!')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001852649500'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'movies4uu1')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001852649500')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://given-collete-movies4u1-ad0fa026.koyeb.app/")



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 1800))
DOWNLOAD_TEXT_URL = "https://t.me/movies4uu2"
CAPTION_BUTTON_URL = "https://t.me/nonstopcinema02"
WEBHOOK = bool(environ.get("WEBHOOK", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "True")
RemoveBG_API = environ.get("RemoveBG_API", "eQ9W36MSu3pmQJLVPZHmF47F")
PM_IMDB = environ.get('PM_IMDB', "True")
REQ_SUB = bool(environ.get("REQ_SUB", True))
PMFILTER = environ.get('PMFILTER', "True")
FILE_REQ_CHANNEL = int(environ.get('FILE_REQ_CHANNEL', LOG_CHANNEL))
#HRK_APP_NAME = environ.get('HRK_APP_NAME', 'NovaXTG')
#HRK_API = environ.get('HRK_API', 'ac75625f-551a-4f5e-e7a2321e792c')

