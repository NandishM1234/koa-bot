
def get_response(message: str) -> str:
    p_message = message.lower()
    checks = ['release', 'released']
    word = 0
    dev_year = 2079
    dev_month_count = 0
    dev_month =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    while word < len(checks):
        if checks[word] in p_message:
            try:
                word = 0
                return (('#faq-and-information' "\n"
                         '**-How long until KoA releases?**' "\n"
                         'It is impossible to answer this right now, it is still a long time until then.'
                         ' The mod tools have accelerated our production, but we can\'t and won\'t give a date.'))
            finally:
                if dev_month_count < len(dev_month):
                    dev_month += 1
                    print(('The release date estimate is extended by an month!'
                           f'It will release in {dev_month[dev_month_count]} {dev_year}'))
                elif dev_month_count == 12:
                    dev_month_count = 0
                    dev_year += 1
                    print(('The release date estimate is extended by an month!'
                           f'It will release in {dev_month[dev_month_count]} {dev_year}'))
        else:
            word += 1
