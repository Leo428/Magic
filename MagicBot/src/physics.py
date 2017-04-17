'''
Created on Apr 14, 2017

@author: huzhe
'''
from pyfrc.physics import drivetrains
import robotMap as rMap

class PhysicsEngine(object):
    '''
       Simulates a 4-wheel robot using Tank Drive joystick control 
    '''
    
    
    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''
        
        self.physics_controller = physics_controller
        self.physics_controller.add_analog_gyro_channel(1)
            
    def update_sim(self, hal_data, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated.
            
            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''
        
        # Simulate the drivetrain
        # -> CANTalon values are from -1023..1023, scale it to -1..1
        lr_motor = hal_data['CAN'][rMap.conf_leftRearBaseTalon]['value'] / 1023
        rr_motor = hal_data['CAN'][rMap.conf_rightRearBaseTalon]['value'] / 1023
        lf_motor = hal_data['CAN'][rMap.conf_leftFrontBaseTalon]['value'] / 1023
        rf_motor = hal_data['CAN'][rMap.conf_rightFrontBaseTalon]['value'] / 1023
        
        # remember, if we use setInverted in the code, then we have to invert
        # the motor outputs in simulation too!
        lr_motor *= -1
        lf_motor *= -1
        
        speed, rotation = drivetrains.four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)