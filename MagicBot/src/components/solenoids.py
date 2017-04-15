'''
Created on Apr 14, 2017

@author: huzhe
'''

from wpilib import DoubleSolenoid
import robotMap as rMap

class Solenoids:
    shiftBaseSolenoid = DoubleSolenoid(rMap.conf_shifterSolenoid1, rMap.conf_shifterSolenoid2)
    liftSolenoid = DoubleSolenoid(rMap.conf_liftSolenoid1, rMap.conf_liftSolenoid2)
    eso = DoubleSolenoid(rMap.conf_esophagusSolenoid1, rMap.conf_esophagusSolenoid2)
    
    shiftState = 0
    
    def __init__(self):
        self.shiftState = self.shiftBaseSolenoid.get()

    
    def setShift(self):
        if self.shiftBaseSolenoid.get() == DoubleSolenoid.Value.kForward:
            self.shiftState = DoubleSolenoid.Value.kReverse
         
        elif self.shiftBaseSolenoid.get() == DoubleSolenoid.Value.kReverse:
            self.shiftState = DoubleSolenoid.Value.kForward
            
        return self.shiftState
    
    def execute(self):
        self.shiftBaseSolenoid.set(self.setShift())
        self.shiftState = self.shiftBaseSolenoid.get()