import pygame # currently unable to install pygame 
import sys
import json
import hashlib

"""
.. module:: dummyrenderer
   :synopsis: This module contains an example Renderer for MPIScope.

.. moduleauthor:: David E. Shere <david.e.shere@gmail.com>

"""


class DummyRenderer:
    """ This class is a mimimal implementation of a Renderer
        for MPIScope.
    """


    def __init__(self):
        """Any initialization goes here
        """
        # Initialize job variables:
        # name, qtime, queue, jobstate, walltimereq
        # start_time, job_owner
        return

    def start(self):
        """Do any initialization required
        """
        return

    def parse(self, data):
        """Do something to the data
        """
        # Filter out null if needed
        return data

    def draw(self, jobData):
        """Do any drawing you want displayed.
           This method is only called when the
           UpdateThread actually has data (IE: is not None)
        """
        # Draw background of circle w/ various radial lines
        # Create square for job, color based on hex of characters
        # Place square based on start_time, figure out coordinates
        return

    def flip(self):
        """Do anything that needs to happen after drawing.
           This method is run every tick even if there is no data.
        """
        return
