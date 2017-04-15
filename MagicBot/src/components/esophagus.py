'''
Created on Apr 14, 2017

@author: zheyuan
'''
from wpilib import DoubleSolenoid
import robotMap as rMap
class Esophagus:
#     shifterSolenoid = DoubleSolenoid(rMap.conf_shifterSolenoid1, rMap.conf_shifterSolenoid2)
#     liftSolenoid = DoubleSolenoid(rMap.conf_liftSolenoid1, rMap.conf_liftSolenoid2)
    esophagusSolenoid = DoubleSolenoid(rMap.conf_esophagusSolenoid1, rMap.conf_esophagusSolenoid2)
    
    def __init__(self):
        pass
    
    def toggleEso(self):
        return self.esophagusSolenoid.get()
    
#     def shiftBase(self):
#         if self.shifterSolenoid.get() == DoubleSolenoid.Value.kReverse:
#             self.shifterSolenoid.set(DoubleSolenoid.Value.kForward)
#         elif self.shifterSolenoid.get() == DoubleSolenoid.Value.kForward:
#             self.shifterSolenoid.set(DoubleSolenoid.Value.kReverse)
#     
#     def engagelift(self):
#         if self.leftJoy.getRawButton(1):
#             if self.liftSolenoid.get() == DoubleSolenoid.Value.kReverse:
#                 self.liftSolenoid.set(DoubleSolenoid.Value.kForward)
#         elif self.liftSolenoid.get() == DoubleSolenoid.Value.kForward:
#             self.liftSolenoid.set(DoubleSolenoid.Value.kReverse)
    
    def execute(self):
        if self.toggleEso() == DoubleSolenoid.Value.kReverse:
            self.esophagusSolenoid.set(DoubleSolenoid.Value.kForward)
        elif self.toggleEso() == DoubleSolenoid.Value.kForward:
            self.esophagusSolenoid.set(DoubleSolenoid.Value.kReverse)
            