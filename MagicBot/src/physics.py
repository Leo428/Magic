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
        lr_motor = hal_data['CAN'][rMap.conf_leftRearBaseTalon]['value']
        rr_motor = hal_data['CAN'][rMap.conf_rightRearBaseTalon]['value']
        lf_motor = hal_data['CAN'][rMap.conf_leftFrontBaseTalon]['value']
        rf_motor = hal_data['CAN'][rMap.conf_rightFrontBaseTalon]['value']
        
        
        speed, rotation = drivetrains.four_motor_drivetrain(lf_motor, rr_motor, lr_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)