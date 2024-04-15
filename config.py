# Overall project configuration file.

"""
| DATA PROCESSOR |
defines, which function will be user for processing data
after retrieval from service.
"""
# DATA_PROCESSOR = "json"  # saves fetched data in json.
DATA_PROCESSOR = "ftp" # sends fetched data to ftp.

"""
| OTHER CONFIG |
INDENT_FOR_SAVED_JSON_DATA - indentation level for *.json files, where fetched data will be saved.
							 The smaller indent level will be used, the less memory will files take.
							 min.value=0
TIMEZONE - timezone, which is used in saved posts.
NUMBER_OF_MESSAGES_TO_SAVE - max.number of retrieved messages per channel, which may store in memory
							 before being dump in local dir or ftp server by DATA_PROCESSOR
USE_PREDEFINED_REQUESTS - should programm use predefined configuration for posts fetcher or
										   use external service to get this data.
DEBUG_MODE - defines if we run programm in debug mode or production. Debug logs will also be added to logfile.
COMMENTS_ENABLED - defines if posts should contain comments or programm could omit them.
QUEUE_READ_SLEEP_TIME - time between each time programm tries to read messages from queue.
LOG_ENABLED - enables/disables write in log.
WRITE_LOG_IN_STDOUT - defines where to write log. stdout or file.
COMMENTS_LIMIT - limit for saved comments per post. [works only when COMMENTS_ENABLED=True].
				 set -1 to have no limit.
"""
INDENT_FOR_SAVED_JSON_DATA = 4
TIMEZONE = "Europe/Kiev"
NUMBER_OF_MESSAGES_TO_SAVE = 100
USE_PREDEFINED_REQUESTS = True
DEBUG_MODE = True
COMMENTS_ENABLED = True
COMMENTS_LIMIT = -1
QUEUE_READ_SLEEP_TIME = 1  # in seconds
LOG_ENABLED = True
WRITE_LOG_IN_STDOUT = True

# ****** Rarely Used Config ****** #

"""
| SERVICE NAME |
defines, which service(fetcher) will be used
for retrieving data.
"""
SERVICE_NAME = "telegram"
# SERVICE_NAME = "twitter" # NOT IMPLEMENTED YET
# SERVICE_NAME = "whatsup" # NOT IMPLEMENTED YET
# SERVICE_NAME = "viber"   # NOT IMPLEMENTED YET

"""
| SESSION |
path to session file. (is used in telegram fetcher)
"""
SESSION = "./tmp/anon"

"""
|*_PATH |
pathes to important locations.
RETRIVED_DATA_STORAGE_PATH - where retrieved data will be saved(in case DATA_PROCESSOR == "json")
FTP_SAVE_DIR_PATH - where retrieved data will be saved(in case DATA_PROCESSOR == "ftp")
LOG_PATH - where logs will be saved.
"""
RETRIVED_DATA_STORAGE_PATH = "./tmp/retrieved_data/"
LOG_PATH = "./tmp/logs/"
FTP_SAVE_DIR_PATH = "./upload"

IS_BACKFILL = False # TODO: this is crutch. need to be refactored