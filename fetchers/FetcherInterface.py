# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Interface to Fetcher class.
#           It is responsible for fetching data from services.
# 			Each service fetcher (telegram fetcher) should inherit this interface.
from datetime import datetime


class FetcherInterface:
    @abstractmethod
    def get_last_post(self):
        pass

    @abstractmethod
    def get_last_n_posts(self, num: int):
        pass

    @abstractmethod
    def get_posts_by_date_range(self, from_date: datetime, to_date: datetime):
        pass

    @abstractmethod
    def get_posts_by_date(self, date: datetime):
        pass

    @abstractmethod
    def get_post_by_id(self, pid: int):
        pass
