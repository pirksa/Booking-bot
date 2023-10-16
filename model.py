class Country:
    country_id: int
    country_code: str
    country_name: str

    def __init__(self, **props):
        self.country_id = props.get('country_id')
        self.country_code = props.get('country_code')
        self.country_name = props.get('country_name')

    def __str__(self):
        return f"Country({self.country_id}, {self.country_code}, {self.country_name})"

    def __eq__(self, other):
        if isinstance(other, Country):
            other = other.country_id, other.country_code, other.country_name
        return (self.country_id, self.country_code, self.country_name) == other


class City:
    city_id: int
    city_code: str
    city_name: str
    timezone: str
    country_id: int

    def __init__(self, **props):
        self.city_id = props.get('city_id')
        self.city_code = props.get('city_code')
        self.city_name = props.get('city_name')
        self.timezone = props.get('timezone')
        self.country_id = props.get('country_id')

    def __str__(self):
        return f'City({self.city_id}, {self.city_code}, {self.city_name}, {self.timezone}, {self.country_id})'

    def __eq__(self, other):
        if isinstance(other, City):
            other = other.city_id, other.city_code, other.city_name, other.timezone, other.country_id
        return self.city_id, self.city_code, self.city_name, self.timezone, self.country_id == other
