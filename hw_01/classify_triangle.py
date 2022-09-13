import unittest

def classify_triangle(a, b, c):
    if a+b > c and b+c > a and a+c>b and a > 0 and b > 0 and c > 0:
        if ((a*a + b*b) == (c*c)):
            return "Right"
        elif(a == b and b == c and a == c):
            return "Equilateral"
        elif(a != b and b != c and a != c):
            return "Scalene"
        else:
            return "Isoceles"
    else:
        return "NotATriangle"

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=', classify_triangle(a,b,c), sep="")

class TestTriangles(unittest.TestCase):
    def testRightTriangle(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(8,15,17),'Right','8,15,17 is a Right triangle')
        self.assertNotEqual(classify_triangle(2,3,4),'Right','2,3,4 is not a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        self.assertEqual(classify_triangle(19,19,19),'Equilateral','19,19,19 is an Equilateral triangle')
        self.assertNotEqual(classify_triangle(2,2,22),'Equilateral','2,2,22 is not an Equilateral triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(4,6,8),'Scalene','4,6,8 is a Scalene triangle')
        self.assertEqual(classify_triangle(15,34,32),'Scalene','15,34,32 is a Scalene triangle')
        self.assertNotEqual(classify_triangle(15,15,15),'Scalene','15,15,15 is not a Scalene triangle')

    def testIsocelesTriangle(self): 
        self.assertEqual(classify_triangle(6,6,8),'Isoceles','6,6,8 is a Isoceles triangle')
        self.assertEqual(classify_triangle(4,6,6),'Isoceles','4,6,6 is a Isoceles triangle')
        self.assertNotEqual(classify_triangle(21,12,14),'Isoceles','21,12,14 is not a Isoceles triangle')

    def testNotATriangleTriangle(self): 
        self.assertEqual(classify_triangle(4,5,10),'NotATriangle','4,5,10 is NotATriangle')
        self.assertEqual(classify_triangle(4,4,8),'NotATriangle','4,4,8 is NotATriangle')
        self.assertNotEqual(classify_triangle(21,21,21),'NotATriangle','21,12,14 is a triangle')
    

if __name__ == '__main__':

    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    