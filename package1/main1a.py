#!python3 -m setuptest.package1.main1a

from setuptest.package1.module1 import func1
from setuptest.package2.module2 import func2

print ("func1", func1(), "func2", func2())


