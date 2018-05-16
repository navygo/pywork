#!/usr/bin/env python3

class Account(object):
    """ zh
    account dollar
    """
    def __init__(self,rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """ zh dollar"""
        return self.__amt

    @property
    def cny(self):
        """zh cny """
        return self.__amt * self.rate

    @amount.setter
    def amount(self,value):
        if value < 0:
            print("Sorry,no negative amount in the account.")
            return 
        self.__amt = value
    @amount.setter
    def lamount(self,value):
        if value < 0:
            print("Sorry,no negative amount in the account.")
            return 
        self.__amt = value

if __name__=='__main__':
    acc =Account(rate=6.7)
    acc.amount = 20
    print("Dollar amount:",acc.amount)
    print("In CNY:",acc.cny)
    acc.amount = -100
    print("Dollar amout:",acc.amount)
    acc.lamount=2000
    print("Dollar amout:",acc.amount)
