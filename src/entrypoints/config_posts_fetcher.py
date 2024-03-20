# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Mocked data for PostsFetcher configurator

# uncomment predefined_config,
# which you want to use and comment all other

from datetime import datetime, timedelta

_current_date = datetime.now().date()
_two_days_ago = _current_date - timedelta(days=2)

# _channels = ["ssternenko", "russvolcorps", "ded_shinibi"]

_channels = [
    "ssternenko",
    "ukrpravda_news",
    "Crimeanwind",
    "DeepStateUA",
    "TCH_channel",
    "uniannet",
    "serhiyprytula",
    "fighter_bomber",
    "romanov_92",
    "SeaPower",
    "strelkovii",
    "millettvcrimea",
    "ZA_FROHT",
    "tass_agency",
    "rian_ru",
    "mod_russia",
    "rsotmdivision",
    "rybar",
    "BILD_Russian",
    "rferl",
]

# predefined_config = {
#     "channels": _channels,
#     "function": "get_last_post",
#     "params": {},
# }

predefined_config = {
    "channels": _channels,
    "function": "get_last_n_posts",
    "params": {"num": 5},
}

# predefined_config = {
#     "channels": _channels,
#     "function": "get_posts_by_date_range",
#     "params": {"from_date": _two_days_ago, "to_date": _current_date},
# }

# predefined_config = {
#     "channels": _channels,
#     "function": "get_posts_by_date",
#     "params": {"date": _two_days_ago},
# }

# predefined_config = {
#     "channels": _channels,
#     "function": "get_post_by_id",
#     "params": {"pid": 123}, # TODO: paste id of real message.
# }
