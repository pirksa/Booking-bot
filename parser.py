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
    city_code, city_name, timezone, country_code = [words[i] for i in range(len(words))]
    return city_code.upper(), city_name.title(), timezone.upper(), country_code.upper()
