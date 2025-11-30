from fastapi import APIRouter
from datetime import datetime
router = APIRouter()

def get_day(date: datetime):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    today_day = days.get(int(date.isoweekday()))
    return today_day

@router.get('/')
def get_current_day(date: datetime):
    today_day = get_day(date)
    return f"Todays day is {today_day}"


