# -----------------------------------------------------------------
# Assignment Name:      SnowBoard and Skis Rental Shop
# Name:                 Kultegh Singh
# -----------------------------------------------------------------

# ------------------------------------------------------------------
# Project 2 Class Area
# ------------------------------------------------------------------
class CustomerClass(object):
    _intTotalItemsRented = int(0)
    _intOrderItemsRented = int(0)
    _dblDiscount = float(0)

    # ------------------------------------------------------------------
    # CustomerClass constructor
    # ------------------------------------------------------------------
    def __init__(self, strName, intID, intRentalTime, strRentalBasis,
                 intSkisRented=0, intSnowboardsRented=0,
                 strCouponCode="", dtmRentalStart=0):
        self.strName = strName
        self.intID = intID
        self.intRentalTime = intRentalTime
        self.strRentalBasis = strRentalBasis
        self.intSkisRented = intSkisRented
        self.intSnowboardsRented = intSnowboardsRented
        self.strCouponCode = strCouponCode
        self.dtmRentalStart = dtmRentalStart

    def __str__(self):
        return "The Customer is renting {} items".format(CustomerClass._intTotalItemsRented)

    def __repr__(self):
        strRepr = (
            "Name: {} \nID: {} \nRental Duration: {}, {}\n# of Skis rented: {} \n# of Snowboards rented: {}"
            "\nCoupon code: {}".format(self.strName, self.intID, self.intRentalTime,
                                        self.strRentalBasis, self.intSkisRented,
                                        self.intSnowboardsRented, self.strCouponCode)
        )
        return strRepr

    # ------------------------------------------------------------------
    # Property: strName
    # ------------------------------------------------------------------
    @property
    def strName(self):
        return self._strName

    @strName.setter
    def strName(self, strInput):
        if str(strInput).isdecimal() is False:
            self._strName = strInput
        else:
            self._strName = ""
            raise Exception("The Name has to contain letters. Value: {}".format(strInput))

    # ------------------------------------------------------------------
    # Property: intID
    # ------------------------------------------------------------------
    @property
    def intID(self):
        return self._intID

    @intID.setter
    def intID(self, intInput):
        if intInput < 0:
            raise Exception("The ID must be greater than 0. Value: {}".format(intInput))
        else:
            self._intID = intInput

    # ------------------------------------------------------------------
    # Property: intSkisRented
    # ------------------------------------------------------------------
    @property
    def intSkisRented(self):
        return self._intSkisRented

    @intSkisRented.setter
    def intSkisRented(self, intInput):
        if isinstance(intInput, int) and intInput >= 0:
            self._intSkisRented = intInput
        else:
            raise Exception("Skis Rented must be a non-negative integer. Value: {}".format(intInput))

    # ------------------------------------------------------------------
    # Property: intSnowboardsRented
    # ------------------------------------------------------------------
    @property
    def intSnowboardsRented(self):
        return self._intSnowboardsRented

    @intSnowboardsRented.setter
    def intSnowboardsRented(self, intInput):
        if isinstance(intInput, int) and intInput >= 0:
            self._intSnowboardsRented = intInput
        else:
            raise Exception("Snowboards Rented must be a non-negative integer. Value: {}".format(intInput))

    # ------------------------------------------------------------------
    # Property: intRentalTime
    # ------------------------------------------------------------------
    @property
    def intRentalTime(self):
        return self._intRentalTime

    @intRentalTime.setter
    def intRentalTime(self, intInput):
        if isinstance(intInput, int) and intInput >= 0:
            self._intRentalTime = intInput
        else:
            raise Exception("Rental Time must be a non-negative integer. Value: {}".format(intInput))

    # ------------------------------------------------------------------
    # Property: strRentalBasis
    # ------------------------------------------------------------------
    @property
    def strRentalBasis(self):
        return self._strRentalBasis

    @strRentalBasis.setter
    def strRentalBasis(self, strInput):
        if strInput in ["Hourly", "Daily", "Weekly"]:
            self._strRentalBasis = strInput
        else:
            raise Exception("Rental basis must be 'Hourly', 'Daily', or 'Weekly'. Value: {}".format(strInput))

    # ------------------------------------------------------------------
    # Property: strCouponCode
    # ------------------------------------------------------------------
    @property
    def strCouponCode(self):
        return self._strCouponCode

    @strCouponCode.setter
    def strCouponCode(self, strInput):
        if str(strInput).isdecimal() is False:
            self._strCouponCode = strInput
        else:
            self._strCouponCode = ""
            raise Exception("Coupon code must contain letters. Value: {}".format(strInput))
