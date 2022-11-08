dev_year = 2079
dev_month_count = 10


def get_release_date():
    global dev_year
    global dev_month_count
    dev_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    if dev_month_count in range(0, 11):
        dev_month_count += 1
        month = dev_month[dev_month_count]
        return (('1 month of dev time has been added! '
                 'The new expected release date is {} {}'.format(month, dev_year)))
    else:
        dev_month_count = 0
        dev_year += 1
        month = dev_month[dev_month_count]
        return (('1 month of dev time has been added! '
                 'The new expected release date is {} {}'.format(month, dev_year)))
