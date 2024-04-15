from src.entities.Request import Request, RequestCode, RequestData
from src.utils.Logger import logger
from datetime import datetime


def adopt_request_to_task_format(request):
    res = {
        "channels": [request["telegram_channel_id"]],
        "function": "get_posts_by_date_range",
        "params": {"from": request["from"], "to": request["to"]},
    }
    return res


def convert_predefined_config_to_request(predefined_config) -> Request:
    error_msg = ""
    result = RequestCode.OK

    channels = []
    name = ""
    params = {}
    is_backfill = False

    if "channels" in predefined_config.keys():
        channels = predefined_config["channels"]
    else:
        result = RequestCode.ERROR
        error_msg = "No channels in predefined config"

    if "function" in predefined_config.keys():
        name = predefined_config["function"]
    else:
        result = RequestCode.ERROR
        error_msg = "No function in predefined config"

    if "params" in predefined_config.keys():
        params = predefined_config["params"]
    else:
        result = RequestCode.ERROR
        error_msg = "No params in predefined config"

    if "is_backfill" in predefined_config.keys():
        is_backfill = predefined_config["is_backfill"]
    else:
        result = RequestCode.ERROR
        error_msg = "No is_backfill in predefined config"

    rdata = RequestData(channels=channels, name=name, params=params, is_backfill=is_backfill)
    ret_request = Request(code=result, data=rdata, rid=0, error_msg=error_msg)
    return ret_request


def convert_message_to_request(message):
    error_msg = ""
    result = RequestCode.OK

    channels = []
    name = "get_posts_by_date_range"
    params = {}
    is_backfill = False

    if "telegram_channel_id" in message.keys():
        channels = [message["telegram_channel_id"]]
    else:
        result = RequestCode.ERROR
        error_msg = "No channel field in message"

    if "is_backfill" in message.keys():
        is_backfill = message["is_backfill"]

    try:
        if "from" in message.keys() and "to" in message.keys():
            _from_date_str = message["from"]
            _to_date_str = message["to"]
            # _from_date = datetime.strptime(_from_date_str, "%Y-%m-%d")
            # _to_date = datetime.strptime(_to_date_str, "%Y-%m-%d")
            _from_date = datetime.fromisoformat(_from_date_str)
            _to_date = datetime.fromisoformat(_to_date_str)
            params["from"] = _from_date
            params["to"] = _to_date
        else:
            result = RequestCode.ERROR
            error_msg = "No date fields(from/to) in message:"
    except Exception as e:
        logger.error(f"Error occured during date conversation: {e}")

    rdata = RequestData(
        channels=channels, name=name, params=params, is_backfill=is_backfill
    )
    ret_request = Request(code=result, data=rdata, rid=0, error_msg=error_msg)
    return ret_request

def convert_str_to_date(s: str):
    d = datetime.fromisoformat(s)
    return d