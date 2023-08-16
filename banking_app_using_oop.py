#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:56:07 2023

@author: ewstott
"""

# Parent Class: User
# Holds details about a user - done
# Has a function to show users details - done

# Child class: Bank
# Stores details about the account balance - done
# Stores details about the amount - done
# Allows for deposits, withdraw, view_balance - done

# Parent class


class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method (aka Function within a class)
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# Child class (inherits properties from User class)


class Bank(User):
    def __init__(self, name, age, gender):
        # << super used to call a method from the parent class when working with inheritance.
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: £", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: £", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: £", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance: £", self.balance)


# Ewan = Bank("Ewan", 30, "Male")
# Ewan.deposit(1000)
# Ewan.withdraw(1200)
# Ewan.view_balance
