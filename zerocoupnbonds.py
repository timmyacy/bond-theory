class ZeroCouponBonds:

    def __init__(self, principal, maturity_rate, number_of_years):
        """
        :param principal: Issue price of the bond
        :param maturity_rate: Bond maturity rate
        :param number_of_years: Time till Bond maturity
        """

        self.principal = principal
        self.maturity_rate = maturity_rate
        self.number_of_years = number_of_years

    def present_value(self, principal, n):
        # Calculate the present value of the bond from the issue price
        return principal / (1 + (self.maturity_rate / 100)) ** n

    def calculate_price(self):
        return self.present_value(self.principal, self.number_of_years)


if __name__ == '__main__':
    bond = ZeroCouponBonds(1000, 2, 4)
print("The present value of the bond is",
      bond.calculate_price())
