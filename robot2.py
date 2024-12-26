#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import time
import wpilib
import wpilib.drive
import rev


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #self.drive = wpilib.SparkMax(11)
        #self.rightDrive = wpilib.PWMSparkMax(1)
        #self.robotDrive = wpilib.drive.DifferentialDrive(
        #    self.leftDrive, self.rightDrive
        #)
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()


        driveMotorChannel = 11
        self.drive : rev.SparkMax = rev.SparkMax(driveMotorChannel, rev.SparkMax.MotorType.kBrushless)
        #self.turningSparkMax: rev.SparkMax = rev.SparkMax(turningMotorChannel, rev.SparkMax.MotorType.kBrushless)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        #self.rightDrive.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        return
        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()  # Stop robot

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        #val = self.controller.getLeftX()

        #self.drive.set(abs(val))
        e = (int(time.time()) % 2) == 0
        if e:
            print('hello')
        #self.robotDrive.arcadeDrive(
        #    -self.controller.getLeftY(), -self.controller.getRightX()
        #)

    def testInit(self):
        """This function is called once each time the robot enters test mode."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass
