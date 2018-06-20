import datetime

old_date = ""

while(1):
    dt = datetime.datetime.now()
    new_date =dt.strftime("%Y-%m-%d %H:%M:%S")
    if new_date != old_date:
        print(new_date)
    old_date = new_date