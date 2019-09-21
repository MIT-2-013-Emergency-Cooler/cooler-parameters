# Copyright 2019 2.013
# Jacob Miske
# !/usr/bin/python3

import cmd
import sys
import os
import getpass
from pyfiglet import Figlet
import matplotlib.pyplot as plt


class CoolerParams:
    """
    Class for functions related to modelling cooler.
    """

    def __init__(self):
        self.energy = 0
        self.questions = ["What is the internal volume? [m^3]",
                          "What is the average heat capacity of the item stored in the cooler?",
                          "How many kgs of that item are there? [kg]",
                          "What is the density of that item? [kg/m^3]",
                          "What average temperature is the cooler volume at? [degrees C]",
                          "What is the convection heat transfer coefficient in the cooler? [W/m^2 C]",
                          "What is the emissivity of the item stored in the cooler?",
                          "What is the thickness of the cooler inner surface [m]",
                          "What is the k of the cooler inner surface? [W/m C]",
                          "What is the thickness of the cooler walls? [m]",
                          "What is the k of the cooler walls? [W/m C]",
                          "What is the thickness of the cooler outer surface? [m]",
                          "What is the k of the cooler outer surface? [W/m C]",
                          "What is the convection heat transfer coefficient outside the cooler? [W/m^2 C]",
                          "What is the emissivity of the cooler outer surface?"
                          "What is the ambient temperature outside the cooler?"
                          ]

    def get_cooler_params(self):
        """Asks a series of questions from user to get information on fridge in question.

        :return:
        """
        cooler_params = []
        print("Welcome to Cooler Params Questions. \n Let's define a small cubic volume as an estimate on how much energy we'll need to cool it. \n")
        for i in range(len(self.questions)):
            while True:
                try:
                    print(self.questions[i])
                    question_answer = float(input("\n"))
                    cooler_params.append(i)
                    break
                except ValueError:
                    print("I didn't get that, try again.")


        return cooler_params