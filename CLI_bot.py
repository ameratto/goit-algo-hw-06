from dataclasses import dataclass
from collections import UserDict
import re
from os.path import join


@dataclass
class Furniture:
    material: str
    weight: float
    height: float
    width: float
    length: float
    _cost: float

    def calculate_discount(self, customer):
        return self._cost - customer.get_discount()/100 * self._cost

class Customer(UserDict):
    def get_discount(self):
        return float(re.search(r'\d', self.data["discount"]).group())

    def get_first_name(self):
        return self.data['name'].split()[0]

    def get_last_name(self):
        return self.data['name'].split()[1]

    def get_email(self):
        return self.data['email']


# class Particle:
#     def __init__(self):
#         self._weight = 0.0
#         self._velocity = 0.0
#         self._acceleration = 0.0
#
#     def get_weight(self):
#         return self._weight
#
#     def get_velocity(self):
#         return self._velocity
#
#     def get_acceleration(self):
#         return self._acceleration
#
#     #@reduction_to_ftype
#     def set_weight(self, weight):
#         self._weight = weight
#
#     #@reduction_to_ftype
#     def set_velocity(self, velocity):
#         self._velocity = velocity
#
#     #@reduction_to_ftype
#     def set_acceleration(self, acceleration):
#         self._acceleration = acceleration


def main():
    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "age": "26",
            "phone": "(992) 914-3792",
            "discount": "10%"
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "age": "18",
            "phone": "(294) 840-6685",
            "discount": "10%"
        },
        {
            "name": "Kennedy Lane",
            "email": "mattis.Cras@nonenimMauris.net",
            "age": "101",
            "phone": "(542) 451-7038",
            "discount": "10%"
        }
    ]

    users = [Customer(el) for el in contacts]
    chair = Furniture("Wood", 20.2, 205.0, 41.1, 60.0, 2000.99)

    print(f"Cost of {chair} for {users[0]['name']}: {chair.calculate_discount(users[0])}")


if __name__ == '__main__':
    main()
