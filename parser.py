def words_list(s: str) -> list:
    punc_index = max(s.find(','), s.find(';'))
    if punc_index != -1:
        s = s.replace(s[punc_index], ' ')
    return s.lower().split()


def country_pars(s: str) -> tuple:
    words = words_list(s)
    country_code, country_name = words[0], ' '.join(words[1:])
    return country_code.upper(), country_name.title()


def city_pars(s: str) -> tuple:
    words = words_list(s)
    city_code, timezone = words[0], words[-1]
    city_name = ' '.join(words[1:-1]) if len(words) > 3 else words[1]
    return city_code.upper(), city_name.title(), timezone.upper()
