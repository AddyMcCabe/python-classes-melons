"""This file should have our melon-type classes in it."""


class WatermelonOrder:
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.0 * qty
        if qty >= 3:
            total = total * 0.75
        return total


class CantaloupeOrder:
    species = "Cantaloupe"
    color = "tan"
    imported = "False"
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.0 * qty
        if qty > 5:
            total / 2
        return total


class CasabaOrder:
    species = "Casaba"
    color = "green"
    imported = "True"
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):
        total = (6.0 * 1.5) * qty
        return total

class SharlynOrder:
    species = "Sharlyn"
    color = "tan"
    imported = "True"
    shape = "natural"
    seasons = "Summer"

    def get_price(self, qty):
        total = 5.0 * qty
        return total


class SantaClausOder:
    species = "Santa Claus"
    color = "green"
    imported = "True"
    shape = "natural"
    seasons = ["Winter", "Spring"]