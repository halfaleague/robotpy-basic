#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

from rev import SparkMax

#import commands2
import wpilib

#from robotcontainer import RobotContainer
import time


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        # self.container = RobotContainer()
        self.manual_test_init()


        # Initialize the Xbox controller
        self.controller = CommandXboxController(0)

        # Bind A button to an ExampleCommand
        self.controller.A().whileHeld(ExampleCommand())


    def manual_test_init(self):
        self.driverController = wpilib.XboxController(0)
        self.autonomousCommand = None
        self.current_motor_index = 0
        self.last_time_pressed = time.time()
        # SPARK MAX CAN IDs
        self.ids = [
        ('kFrontLeftDrivingCanId', 10),
        ('kFrontLeftTurningCanId', 11),

        ('kRearLeftTurningCanId', 15),
        ('kRearLeftDrivingCanId', 16),

        ('kFrontRightTurningCanId', 20),
        ('kFrontRightDrivingCanId', 21),

        ('kRearRightTurningCanId', 25),
        ('kRearRightDrivingCanId', 26),
        ]

        self.motors = {}
        for lbl, cid in self.ids:
            self.motors[cid] = SparkMax(cid, SparkMax.MotorType.kBrushless)

        self.motor_label, self.can_id = self.ids[self.current_motor_index]
        self.motor = self.motors[self.can_id]

        self.on = False

    def autonomousInit(self) -> None:
        pass
        #self.autonomousCommand = self.container.getAutonomousCommand()

        #if self.autonomousCommand:
        #    self.autonomousCommand.schedule()

    def teleopInit(self) -> None:
        pass
        #if self.autonomousCommand:
        #    self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        # Teleop periodic logic
        #self.driveWithJoystick(True)
        pass
        self.tel_manual()

    def tel_manual(self):
        dc = self.driverController
        now = time.time()
        elapsed = now-self.last_time_pressed
        print('elapsed:', elapsed)

        if dc.getBButton() and elapsed >= 1:
            self.current_motor_index += 1
            if self.current_motor_index >= len(self.ids):
                self.current_motor_index = 0
            self.last_time_pressed = now
            self.motor_label, self.can_id = self.ids[self.current_motor_index]
            self.motor = self.motors[self.can_id]

        if dc.getYButton() and elapsed >= 1:
            self.current_motor_index -= 1
            if self.current_motor_index <= -1:
                self.current_motor_index = len(self.ids) - 1
            self.last_time_pressed = now
            self.motor_label, self.can_id = self.ids[self.current_motor_index]
            self.motor = self.motors[self.can_id]

        print(self.motor_label, self.can_id, self.motor)

        if dc.getXButton(): 
            self.motor.set(.5)
        else:
            self.motor.set(0)

        # TODO encoder
        # import phoenix6 as p6 
        # x = p6.hardware.CANcoder(12)
        # p2 = x.get_absolute_position()
        # p2.value # 0-1 value?

    
    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(MyRobot)

