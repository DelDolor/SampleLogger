#!/usr/bin/env python3

""" """

# create class
class Bike:
   # constructor function    
    def __init__(self, name = "not set", gear = "none"):
        self.name = name
        self.gear = 0

    def get_name(self):
        return self.name