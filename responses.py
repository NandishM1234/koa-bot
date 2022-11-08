def get_response(channel, message):
    p_message = message.lower()
    word = 0
    checks = ['release', 'released']
    while word < (len(checks) + 1):
        if checks[word] in p_message:
            return (('#faq-and-information' "\n"
                     '**-How long until KoA releases?**' "\n"
                     'It is impossible to answer this right now, it is still a long time until then.'
                     ' The mod tools have accelerated our production, but we can\'t and won\'t give a date.'))
        else:
            word += 1
