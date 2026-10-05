from datetime import datetime, timezone

def timezone_convert(photo_time_str):
    photo_time_obj = datetime.fromisoformat(photo_time_str)

    photo_time_utc = photo_time_obj.astimezone(timezone.utc).replace(tzinfo=None)

    return photo_time_utc