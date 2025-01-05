#!/usr/bin/env python3

import time
import wpilib
import wpilib.drive
import rev
import navx

import phoenix6



# TODO 

# commands:
# https://github.com/robotpy/examples/blob/main/ArmBot/robotcontainer.py

# navx

# network tables


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.controller = wpilib.XboxController(0)

        self.gyro = navx.AHRS.create_i2c()

        driveMotorChannel = 11
        self.drive11 = rev.SparkMax(driveMotorChannel, rev.SparkMax.MotorType.kBrushless)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        #self.rightDrive.setInverted(True)

        #self.cancoder12 = p6.hardware.CANcoder(12)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""

        #val = self.controller.getLeftX()
        #self.drive.set(abs(val))
        #abs_pos  = self.cancoder12.get_absolute_position()
        #abs_pos.value
        #self.gyro.getAngle()

        e = (int(time.time()) % 2) == 0
        if e:
            print('hello')

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def testInit(self):
        """This function is called once each time the robot enters test mode."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass
