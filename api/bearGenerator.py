from faker import Faker
import random


faker = Faker()
valid_bear_type = ['BROWN', 'BLACK', 'POLAR', 'GUMMY']

def random_valid_bear():
    return {
        "bear_type": random.choice(valid_bear_type),
        "bear_name": faker.first_name(),
        "bear_age": faker.pyint(0, 1000)/10
    }



