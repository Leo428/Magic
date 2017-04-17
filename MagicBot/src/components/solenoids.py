'''
Created on Apr 14, 2017

@author: huzhe
'''

import wpilib

class Solenoids:
    shiftBaseSolenoid = wpilib.DoubleSolenoid
    
    def __init__(self):
        self.shiftState = 0
    
    def setShift(self):
        if self.shiftBaseSolenoid.get() == wpilib.DoubleSolenoid.Value.kForward:
            self.shiftState = wpilib.DoubleSolenoid.Value.kReverse
        
        else:
            self.shiftState = wpilib.DoubleSolenoid.Value.kForward
            
        print(self.shiftState)
        return self.shiftState
    
    def execute(self):
        print('here ' + str(self.shiftState))
        self.shiftBaseSolenoid.set(self.shiftState)
        self.shiftState = self.shiftBaseSolenoid.get()