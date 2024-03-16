# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Is responsible for returning configuration of
# 			 1. what channels to monitor.
# 			 2. which method to use for monitoring. get_posts_by_date, get_last_n_posts.
# 			It can get info from external service as well as predefined data.
# 			The way ExternalConfigurator gets info depends on configuration in config.py


class ExternalConfigurator:
    def get_channels_to_monitor():
        channels = ["ssternenko"]
        return channels
        info = {
            "channels": channels,
            "method": "get_last_n_posts",
        }
