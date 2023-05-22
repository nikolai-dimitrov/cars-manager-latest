from enum import Enum


class BodyType(Enum):
    sedan = 'Sedan'
    touring = 'Touring'
    coupe = 'Coupe'
    suv = 'SUV'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Cylinders:
    CYLINDER_CHOICES = {
        'all': 'All',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '8': '8',
        '10': '10',
        '12': '12',
        '16': '16',
    }

    @classmethod
    def fuel_choices(cls):
        return [(k, v) for k, v in cls.CYLINDER_CHOICES.items()]


class Fuel:
    _AD_CHOICES = {
        'diesel': 'Diesel',
        'petrol': 'Petrol',
        'gas': 'Gas',
    }
    _CAR_SEARCH_CHOICES = {
        'all': 'All',
        'diesel': 'Diesel',
        'gas': 'Gas',
        'electricity': 'Electricity',
    }

    @classmethod
    def choices(cls):
        return [(k, v) for k, v in cls._AD_CHOICES.items()]

    @classmethod
    def car_api_search_choices(cls):
        return [(k, v) for k, v in cls._CAR_SEARCH_CHOICES.items()]


class Transmission:
    _AD_CHOICES = {
        'manual': 'Manual',
        'automatic': 'Automatic',
    }
    _CAR_SEARCH_CHOICES = {
        'all': 'All',
        'm': 'Manual',
        'a': 'Automatic',
    }

    @classmethod
    def choices(cls):
        return [(k, v) for k, v in cls._AD_CHOICES.items()]

    @classmethod
    def car_api_search_choices(cls):
        return [(k, v) for k, v in cls._CAR_SEARCH_CHOICES.items()]
