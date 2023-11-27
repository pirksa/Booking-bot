def country_pars(s: str) -> tuple:
    punc_index = max(s.find(','), s.find(';'))
    if punc_index != -1:
        s = s.replace(s[punc_index], ' ')
    words = s.lower().split()
    country_code = words[0]
    country_name = ' '.join(words[1:])
    return country_code.upper(), country_name.title()
