# Overall project configuration file.

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
| DATA PROCESSOR |
defines, which function will be user for processing data
after retrieval from service.
"""
DATA_PROCESSOR = "json"  # saves fetched data in json.
# DATA_PROCESSOR = "ftp" # sends fetched data to ftp.


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


"""
| OTHER CONFIG |
INDENT_FOR_SAVED_JSON_DATA - indentation level for *.json files, where fetched data will be saved.
							 The smaller indent level will be used, the less memory will files take.
							 min.value=0
TIMEZONE - timezone, which is used in saved posts.
NUMBER_OF_MESSAGES_TO_SAVE - max.number of retrieved messages per channel, which may store in memory
							 before being dump in local dir or ftp server by DATA_PROCESSOR
USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR - should programm use predefined configuration for posts fetcher or
										   use external service to get this data.
DEBUG_MODE - defines if we run programm in debug mode or production. Debug logs will also be added to logfile.
"""
INDENT_FOR_SAVED_JSON_DATA = 4
TIMEZONE = "Europe/Kiev"
NUMBER_OF_MESSAGES_TO_SAVE = 1000
USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR = True
DEBUG_MODE = False
