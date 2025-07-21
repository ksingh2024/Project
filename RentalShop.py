# -----------------------------------------------------------------
# Assignment Name:      SnowBoard and Skis Rental Shop
# Name:                 Kultegh Singh
# -----------------------------------------------------------------


from datetime import datetime

# ------------------------------------------------------------------
# Project 2 Class Area
# ------------------------------------------------------------------
class RentalShop:
    'Class for rental shops that rent out skis and snowboards'

    # Inventory and financial tracking (class-level variables)
    _intTotalSkis = 0
    _intTotalSnowboards = 0
    _intSkisAvailable = 0
    _intSnowboardsAvailable = 0
    _dblDailyRevenue = 0.0
    _intDailySkisRented = 0
    _intDailySnowboardsRented = 0

    # Pricing
    _dblSkiHourlyRate = 15
    _dblSkiDailyRate = 50
    _dblSkiWeeklyRate = 200
    _dblSnowboardHourlyRate = 10
    _dblSnowboardDailyRate = 40
    _dblSnowboardWeeklyRate = 160

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------
    def __init__(self, intTotalSkis, intTotalSnowboards):
        self.intTotalSkis = intTotalSkis
        self.intTotalSnowboards = intTotalSnowboards
        RentalShop._intSkisAvailable = intTotalSkis
        RentalShop._intSnowboardsAvailable = intTotalSnowboards

    # ------------------------------------------------------------------
    # Properties with validation
    # ------------------------------------------------------------------
    @property
    def intTotalSkis(self):
        return self._intTotalSkis

    @intTotalSkis.setter
    def intTotalSkis(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Total skis must be a non-negative integer.")
        self._intTotalSkis = value

    @property
    def intTotalSnowboards(self):
        return self._intTotalSnowboards

    @intTotalSnowboards.setter
    def intTotalSnowboards(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Total snowboards must be a non-negative integer.")
        self._intTotalSnowboards = value

    # ------------------------------------------------------------------
    # Inventory & revenue accessors
    # ------------------------------------------------------------------
    def GetAvailableSkis():
        return RentalShop._intSkisAvailable

    def GetAvailableSnowboards():
        return RentalShop._intSnowboardsAvailable

    def GetDailyRevenue():
        return RentalShop._dblDailyRevenue

    def GetDailySkisRented():
        return RentalShop._intDailySkisRented

    def GetDailySnowboardsRented():
        return RentalShop._intDailySnowboardsRented

    # ------------------------------------------------------------------
    # Convert Date to Time Units
    # ------------------------------------------------------------------
    def ConvertDateToTimeUnits(self, dtmStart, dtmEnd):
        duration = dtmEnd - dtmStart
        hours = int((duration.seconds / 3600) + (duration.days * 24))
        days = 0
        weeks = 0

        while hours >= 24:
            days += 1
            hours -= 24

        while days >= 7:
            weeks += 1
            days -= 7

        if hours > 3:
            days += 1
            hours = 0

        if days > 4:
            weeks += 1
            days = 0
            hours = 0

        return hours, days, weeks

    # ------------------------------------------------------------------
    # Estimate / Bill Calculators
    # ------------------------------------------------------------------
    def CalculateEstimate(self, basis, skis, snowboards, time, coupon=""):
        if basis.lower() == "hourly":
            return self._CalculateBestPrice(time, 0, 0, skis, snowboards, coupon)
        elif basis.lower() == "daily":
            return self._CalculateBestPrice(0, time, 0, skis, snowboards, coupon)
        elif basis.lower() == "weekly":
            return self._CalculateBestPrice(0, 0, time, skis, snowboards, coupon)
        else:
            raise Exception("Rental period must be hourly, daily, or weekly.")

    def CalculateBill(self, dtmStart, dtmEnd, skis=0, snowboards=0, coupon=""):
        hours, days, weeks = self.ConvertDateToTimeUnits(dtmStart, dtmEnd)
        subtotal = self._CalculateSubTotal(hours, days, weeks, skis, snowboards)
        discount = self._CalculateFamilyDiscount(hours, days, weeks, skis, snowboards) \
                 + self._CalculateCouponDiscount(coupon, subtotal)
        total = subtotal - discount
        RentalShop._dblDailyRevenue += total
        return subtotal, discount, total

    def _CalculateSubTotal(self, hours, days, weeks, skis=0, snowboards=0):
        total = 0.0
        total += skis * hours * RentalShop._dblSkiHourlyRate
        total += skis * days * RentalShop._dblSkiDailyRate
        total += skis * weeks * RentalShop._dblSkiWeeklyRate
        total += snowboards * hours * RentalShop._dblSnowboardHourlyRate
        total += snowboards * days * RentalShop._dblSnowboardDailyRate
        total += snowboards * weeks * RentalShop._dblSnowboardWeeklyRate
        return total

    # ------------------------------------------------------------------
    # Discounts
    # ------------------------------------------------------------------
    def _CalculateFamilyDiscount(self, hours=0, days=0, weeks=0, skis=0, snowboards=0):
        total_discount = 0.0
        total_items = skis + snowboards
        discounted = 0

        if 3 <= total_items <= 5:
            total_discount += self._CalculateSkiDiscount(hours, days, weeks, skis)
            total_discount += self._CalculateSnowboardDiscount(hours, days, weeks, snowboards)
        elif total_items > 5:
            while discounted < 5:
                if skis > 0:
                    total_discount += self._CalculateSkiDiscount(hours, days, weeks)
                    skis -= 1
                elif snowboards > 0:
                    total_discount += self._CalculateSnowboardDiscount(hours, days, weeks)
                    snowboards -= 1
                discounted += 1

        return total_discount

    def _CalculateSkiDiscount(self, hours, days, weeks, skis=1):
        return skis * (
            hours * RentalShop._dblSkiHourlyRate * 0.25 +
            days * RentalShop._dblSkiDailyRate * 0.25 +
            weeks * RentalShop._dblSkiWeeklyRate * 0.25
        )

    def _CalculateSnowboardDiscount(self, hours, days, weeks, snowboards=1):
        return snowboards * (
            hours * RentalShop._dblSnowboardHourlyRate * 0.25 +
            days * RentalShop._dblSnowboardDailyRate * 0.25 +
            weeks * RentalShop._dblSnowboardWeeklyRate * 0.25
        )

    def _CalculateCouponDiscount(self, coupon, subtotal):
        if isinstance(coupon, str) and len(coupon) == 6 and coupon[-3:] == "BBP":
            return subtotal * 0.10
        return 0.0

    def _CalculateBestPrice(self, hours=0, days=0, weeks=0, skis=0, snowboards=0, coupon=""):
        if hours > 3:
            days += 1
            hours = 0
        if days > 4:
            weeks += 1
            days = 0
            hours = 0

        subtotal = self._CalculateSubTotal(hours, days, weeks, skis, snowboards)
        discount = self._CalculateFamilyDiscount(hours, days, weeks, skis, snowboards) \
                 + self._CalculateCouponDiscount(coupon, subtotal)
        return subtotal - discount
