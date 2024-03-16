# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Mocked data for PostsFetcher configurator
from datetime import datetime, timedelta

_current_date = datetime.now().date()
_two_days_ago = _current_date - timedelta(days=2)

_chanels = ["ssternenko", "russvolcorps"]

# predefined_config = {
#     "channels": _chanels,
#     "function": "get_last_post",
#     "params": {},
# }

predefined_config = {
    "channels": _chanels,
    "function": "get_last_n_posts",
    "params": {"num": 2},
}

# predefined_config = {
#     "channels": _chanels,
#     "function": "get_posts_by_date_range",
#     "params": {"from_date": _current_date, "to_date": _two_days_ago},
# }

# predefined_config = {
#     "channels": _chanels,
#     "function": "get_posts_by_date",
#     "params": {"date": _current_date},
# }

# predefined_config = {
#     "channels": _chanels,
#     "function": "get_post_by_id",
#     "params": {"pid": 123}, # TODO: paste id of real message.
# }
