from datetime import datetime

date = "2021-07-05T07:00:00+08:00"
        # expected_result = "Monday 05 July 2021"
        # result = weather.convert_date(date)

datestr=datetime.fromisoformat(date)
print(f"{datestr.strftime("%A")} {datestr.strftime("%d")} {datestr.strftime("%B")} {datestr.strftime("%Y")}")
# return f"{weekday}" "{day}" "{month}" "{year}"        
