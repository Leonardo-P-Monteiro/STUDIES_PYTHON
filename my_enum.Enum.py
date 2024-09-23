################################################################################
#################################### ENUMS #####################################
################################################################################
"""
This code was done by me.
"""

from enum import Enum, auto


class SignalColors(Enum):
    RED = 'Stop'
    YELLOW = 'Attencion'
    GREEN = 'Go'

class Signal():
    def __init__(self, name):
        self.name = name
        self.status = SignalColors.RED.value
        self.color = SignalColors.RED.name
    
    def signal_status(self):
        print(f'Signal Colo is: {self.color} ({self.status})')
    
    def change_signal_yellow(self):
        self.status = SignalColors.YELLOW.value
        self.color = SignalColors.YELLOW.name
        
    
    def change_signal_green(self):
        self.status = SignalColors.GREEN.value
        self.color = SignalColors.GREEN.name
    
    def change_signal_red(self):
        self.status = SignalColors.RED.value
        self.color = SignalColors.RED.name
    
################################################################################
################################## OPERATIONS ##################################
################################################################################

s1 = Signal('Signal1')
s1.signal_status()
s1.change_signal_green()
s1.signal_status()
s1.change_signal_yellow()
s1.signal_status()
s1.change_signal_red()
s1.signal_status()