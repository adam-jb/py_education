# python3 -m unittest unit_test.py
import unittest

class Angle():
    def __init__(self, angle):
        self.degrees = angle
        
    def __repr__(self):
        return str(self.degrees) + ' degrees'

class TestAngle(unittest.TestCase): 
    def test_degrees(self):
        small_angle = Angle(60)
        self.assertEqual(60, small_angle.degrees)

