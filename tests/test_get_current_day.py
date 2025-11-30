import pytest
from datetime import datetime
from src.routes.get_current_day_of_week import get_day

sunday = datetime.strptime("26-10-2025", "%d-%m-%Y")
monday = datetime.strptime("27-10-2025", "%d-%m-%Y")

@pytest.mark.parametrize(
    "input_date, exp_result",
    [
        (sunday, "Sunday"),
        (monday, "Monday")
    ]
)
def test_valid_get_day(input_date, exp_result):
    today_day = get_day(input_date)
    assert today_day == exp_result