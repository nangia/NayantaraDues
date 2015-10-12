from abc import ABCMeta, abstractmethod


class BaseInterestModel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getYearInterest(self, year):
        pass

    @abstractmethod
    def description(self):
        pass


class ConstantEightPercent(BaseInterestModel):
    def getYearInterest(self, year):
        return 8.0

    def description(self):
        return "Interest of 8% per annum"


class ConstantTenPercent(BaseInterestModel):
    def getYearInterest(self, year):
        return 10.0

    def description(self):
        return "Interest of 10% per annum"


class ConstantFifteenPercent(BaseInterestModel):
    def getYearInterest(self, year):
        return 15.0

    def description(self):
        return "Interest of 15% per annum"


startyear = 1986
endyear = 2015
awardAmount = 50000.0

amount = awardAmount
models = [ConstantEightPercent(), ConstantTenPercent(), ConstantFifteenPercent()]

for curmodel in models:
    for year in range(startyear, endyear):
        rateofinterest = curmodel.getYearInterest(year)
        amount = amount * (1 + rateofinterest/100)

    print "Nayantara owes Sahitya Academy INR %s (%s) " % ("{:,.2f}".format(amount),
                                                          curmodel.description())
