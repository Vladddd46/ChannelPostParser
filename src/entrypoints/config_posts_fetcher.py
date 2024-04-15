# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Mocked data for PostsFetcher configurator

# uncomment predefined_config,
# which you want to use and comment all other

from datetime import datetime, timedelta

year = 365
two_years = year * 2
days = 50

_current_date = datetime.now().date()
fromdate = _current_date - timedelta(days=days)

_channels = ["DeepStateUA"]#[-1001101170442]#["ded_shinibi"]

# _channels = [
#     "ssternenko",
#     "ukrpravda_news",
#     "Crimeanwind",
#     "DeepStateUA",
#     "TCH_channel",
#     "uniannet",
#     "serhiyprytula",
#     "fighter_bomber",
#     "romanov_92",
#     "SeaPower",
#     "strelkovii",
#     "millettvcrimea",
#     "ZA_FROHT",
#     "tass_agency",
#     "rian_ru",
#     "mod_russia",
#     "rsotmdivision",
#     "rybar",
#     "BILD_Russian",
#     "rferl",
# ]

# predefined_config = {
#     "channels": _channels,
#     "function": "get_last_post",
#     "params": {},
# }

# predefined_config = {
#     "channels": _channels,
#     "function": "get_last_n_posts",
#     "params": {"num": 5},
# }

predefined_config = {
    "channels": _channels,
    "function": "get_posts_by_date_range",
    "params": {"from": fromdate, "to": _current_date},
    "is_backfill": True
}

# predefined_config = {
#     "channels": _channels,
#     "function": "get_posts_by_date",
#     "params": {"date": fromdate},
# }

# predefined_config = {
#     "channels": _channels,
#     "function": "get_post_by_id",
#     "params": {"pid": 123}, # TODO: paste id of real message.
# }
