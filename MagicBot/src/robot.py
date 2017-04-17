#!/usr/bin/env python3
'''
    This is a demo program showing the use of the RobotDrive class.
    
    The SampleRobot class is the base of a robot application that will
    automatically call your Autonomous and OperatorControl methods at
    the right time as controlled by the switches on the driver station
    or the field controls.
    
    WARNING: While it may look like a good choice to use for your code
    if you're inexperienced, don't. Unless you know what you are doing,
    complex code will be much more difficult under this system. Use
    IterativeRobot or Command-Based instead if you're new.
'''

import wpilib
from wpilib import Joystick
from magicbot import MagicRobot
import robotMap as rMap
from ctre import CANTalon
from components.solenoids import Solenoids

isSimulation = MagicRobot.isSimulation()

class MyRobot(MagicRobot):
    solenoids = Solenoids
    def createObjects(self):
        
        self.shiftBaseSolenoid = wpilib.DoubleSolenoid(rMap.conf_shifterSolenoid1, rMap.conf_shifterSolenoid2)
        self.rightFrontBaseMotor = CANTalon(rMap.conf_rightFrontBaseTalon)
        self.rightRearBaseMotor = CANTalon(rMap.conf_rightRearBaseTalon)
        self.leftFrontBaseMotor = CANTalon(rMap.conf_leftFrontBaseTalon)
        self.leftRearBaseMotor = CANTalon(rMap.conf_leftRearBaseTalon)
        
        self.rightFrontBaseMotor.enableControl()
        self.rightRearBaseMotor.enableControl()
        self.rightRearBaseMotor.setControlMode(CANTalon.ControlMode.Follower)
        self.rightRearBaseMotor.set(rMap.conf_rightFrontBaseTalon)
        
        self.leftFrontBaseMotor.enableControl()
        self.leftRearBaseMotor.enableControl()
        self.leftFrontBaseMotor.setInverted(True)
        self.leftRearBaseMotor.setControlMode(CANTalon.ControlMode.Follower)
        self.leftRearBaseMotor.set(rMap.conf_leftFrontBaseTalon)

        self.leftJoy = Joystick(rMap.conf_left_joy)
        self.rightJoy = Joystick(rMap.conf_right_joy)
        self.xbox = Joystick(rMap.conf_xbox)
        
        self.robotDrive = wpilib.RobotDrive(self.leftFrontBaseMotor,self.rightFrontBaseMotor)
    def autonomous(self):
        """Drive left and right motors for two seconds, then stop."""
        MagicRobot.autonomous(self)
        

    def teleopInit(self):
        MagicRobot.teleopInit(self)
    
    def teleopPeriodic(self):
        self.robotDrive.tankDrive(self.leftJoy.getY(),self.rightJoy.getY())
        try:
            if self.leftJoy.getRawButton(7):
                self.solenoids.setShift()
                print("RED " + str(self.solenoids.setShift()))
    
        except:
            self.onException()
            
    def test(self):
        '''Runs during test mode'''
        wpilib.LiveWindow.run()
        
if __name__ == "__main__":
    wpilib.run(MyRobot)
