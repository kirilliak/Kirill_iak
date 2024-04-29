from datetime import datetime
def get_days_from_today(date):
    try:
        date_users = datetime.strptime(date, '%Y-%m-%d').date()
        date_now = datetime.today().date()
        date_difference = date_now - date_users
        return date_difference
    except ValueError:
        return -1
    
print(get_days_from_today("2022-02-24"))