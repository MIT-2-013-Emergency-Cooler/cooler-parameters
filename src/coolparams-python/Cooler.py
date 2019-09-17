# Copyright 2019 2.013
# Jacob Miske
# !/usr/bin/python3

import cmd
import sys
import os
import getpass
from pyfiglet import Figlet
from sim_engine.CoolerSim import CoolerSim


class Cooler(cmd.Cmd):
    """A simple cmd application using cmd.
    """
    custom_fig = Figlet(font='slant')
    intro = 'Welcome to the Cooler shell.  Type help or ? to list commands.\n'
    prompt = '> '
    file = None
    print(custom_fig.renderText('  Cooler Params'))

    def do_status(self, arg):
        """status: Yields device status for the edge device.
        Returns a table of details related to health of unit.
        """
        def status():
            """Runs the list generation
            """
            custom_fig = Figlet(font='slant')
            print(custom_fig.renderText(' status'))
        status()

    def do_whoami(self, arg):
        """Prints out user data
        """
        def whoami():
            print(getpass.getuser())
            print('File Directory')
            cwd = os.getcwd()  # Get the current working directory (cwd)
            files = os.listdir(cwd)  # Get all the files in that directory
            print("Files in '%s': %s" % (cwd, files))
        whoami()

    def do_run_sim(self, arg):
        """Begins prompt for sim engine
        """
        coolsim_obj = CoolerSim()
        coolsim_obj.run_sim_plot()


    def do_bye(self, arg):
        """Stop cmd, close the window, and exit:  BYE
        """
        print("Thank you for using Cooler Params")
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == "__main__":
    c = Cooler()
    sys.exit(c.cmdloop())
