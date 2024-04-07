def adopt_request_to_task_format(request):
    res = {
        "channels": [request["telegram_channel_id"]],
        "function": "get_posts_by_date_range",
        "params": {"from_date": request["from_date"], "to_date": request["to_date"]},
    }
    return res
