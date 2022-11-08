
def get_response(message: str) -> str:
    p_message = message.lower()
    checks = ['release', 'released']
    word = 0
    while word < len(checks):
        if checks[word] in p_message:
            word = 0
            return (('#faq-and-information' "\n"
                     '**-How long until KoA releases?**' "\n"
                     'It is impossible to answer this right now, it is still a long time until then.'
                     ' The mod tools have accelerated our production, but we can\'t and won\'t give a date.'))
        else:
            word += 1
