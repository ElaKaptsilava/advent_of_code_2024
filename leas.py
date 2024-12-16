class Auto:
    def __init__(self, amount_netto: float, percentage_brutto: float):
        self.amount_netto = amount_netto
        self.percentage_brutto = percentage_brutto

    @property
    def amount_brutto(self):
        return round(self.amount_netto * (1 + self.percentage_brutto / 100))


class Leasing:
    def __init__(self, year_per: float, auto: Auto, first_fee_per: float, last_fee_per: float, months_number: int):
        self.year_per = year_per
        self.auto = auto
        self.first_fee_per = first_fee_per
        self.last_fee_per = last_fee_per
        self.months_number = months_number

    def calculate_first_fee_netto(self):
        return self.auto.amount_netto * (self.first_fee_per / 100)

    def calculate_last_fee_netto(self):
        return self.auto.amount_netto * (self.last_fee_per / 100)

    def calculate_first_fee_brutto(self):
        return self.auto.amount_brutto * (self.first_fee_per / 100)

    def calculate_last_fee_brutto(self):
        return self.auto.amount_brutto * (self.last_fee_per / 100)

    def financing_amount_netto(self):
        return auto.amount_netto - self.calculate_first_fee_netto() - self.calculate_last_fee_netto()

    def financing_amount_brutto(self):
        return auto.amount_brutto - self.calculate_first_fee_brutto() - self.calculate_last_fee_brutto()

    @property
    def monthly_percentage(self):
        return self.year_per / 100 / 12

    def calculate_rate_netto(self):
        up = self.financing_amount_netto() * self.monthly_percentage * (
                1 + self.monthly_percentage) ** self.months_number
        down = (1 + self.monthly_percentage) ** self.months_number - 1
        return up / down

    def report(self):
        print("Auto **netto** amount: ", self.auto.amount_netto)
        print("Auto **brutto** amount: ", self.auto.amount_brutto)
        print()
        print("First fee netto amount: ", self.calculate_first_fee_netto())
        print("Last fee netto amount: ", self.calculate_last_fee_netto())


if __name__ == '__main__':
    auto = Auto(43008.13, 23)
    print(auto.amount_brutto)
    leas = Leasing(
        year_per=5.81,
        auto=auto,
        first_fee_per=25,
        last_fee_per=1,
        months_number=36
    )
    print(leas.calculate_rate_netto())
    print(leas.calculate_first_fee_brutto())
    print(leas.calcu)
