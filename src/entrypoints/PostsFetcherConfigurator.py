# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Is responsible for returning configuration of
# 			 1. what channels to monitor.
# 			 2. which method to use for monitoring. get_posts_by_date, get_last_n_posts.
# 			It can get info from external service as well as predefined data.
# 			The way ExternalConfigurator gets info depends on configuration in config.py
from config import USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR
from src.entrypoints.config_posts_fetcher import predefined_config
from src.utils.Logger import logger


class PostsFetcherConfigurator:
    def get_posts_fetcher_configuration(self):
        logger.info(
            f"Getting posts fetcher configuration | use_predefined_data={USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR}"
        )
        ret = None
        if USE_PREDEFINED_POSTSFETCHER_CONFIGURATOR == True:
            ret = predefined_config
        else:
            # TODO: add external configuration service.
            logger.error("External configuration service is not implemented yet.")
            exit(1)
        return ret
