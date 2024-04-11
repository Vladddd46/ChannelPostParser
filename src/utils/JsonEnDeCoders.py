import json
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # Convert datetime to ISO 8601 string format
            return obj.isoformat()
        return super().default(obj)
