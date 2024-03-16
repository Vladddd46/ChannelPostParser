
# variable, that defines, 
# which fetcher will be used for getting posts. 
# For now only 'telegram' service is implemented.
SERVICE_NAME = "telegram"

DATA_PROCESSOR = "json" # dump fetched data in json.
# DATA_PROCESSOR = "ftp" # sends fetched data to ftp.


# path to session file. [used for telegram fetcher]
SESSION = "./tmp/anon"

RETRIVED_DATA_STORAGE_PATH = "./retrieved_data/"

# Indentation level for files.json, where fetched data will be saved
# Use the min value of indent=0 in order to save memory space.
# More symbols in file=More memory needed.
INDENT_FOR_SAVED_JSON_DATA = 0

# path to directory on ftp server, where fetched data will be saved.
FTP_SAVE_DIR_PATH = "./upload"

# path, where logs will be stored
LOG_PATH = "./logs"

TIMEZONE = "Europe/Kiev"


# defines max value of retrieved messages, that should be saved.
NUMBER_OF_MESSAGES_TO_SAVE = 50

USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR = True

