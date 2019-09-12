# Copyright 2019 2.013
# Jacob Miske
# !/usr/bin/python3

import cmd
import sys
import os
import getpass
from pyfiglet import Figlet
import matplotlib.pyplot as plt


class CoolerSim:
    """
    Class for functions related to modelling cooler.
    """

    def __init__(self):
        self.internal_temp = 4      # [C]
        self.external_temp = 25     # [C]
        self.thermal_cond = 10      # [W/(m*C)]
        self.cooler_area = 1        # [m^2]
        self.wall_thick = 0.01      # [m]
        self.sim_time = 600         # [s]

    def get_heat_transfer_rate(self, k, T_in, T_out, thickness):
        """
        Calculates the following functions:
        q = - k dT/dx
        for heat transfer rate from the cooler given parameters
        :return: q
        """
        return -k * (T_in - T_out)/(thickness)

    def get_heat_flux(self, q, area):
        """
        Calculates the following functions:
        Q = qA
        for heat flux from the cooler given parameters
        :return: Q
        """
        return q*area

    def run_sim_plot(self):
        """
        Considers set params and plots them over a time.
        :return:
        """
        x_time = range(self.sim_time)
        y_heat = []
        for i in self.x_time:
            y_heat.append(self.get_heat_flux(self.thermal_cond,
                                             self.internal_temp,
                                             self.external_temp,
                                             self.wall_thick))
        plt.figure(1)
        plt.plot(x_time, y_heat)
        plt.savefig("sim_plot.png")


