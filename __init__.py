# ur_ikfast/__init__.py

# Example: alias one solver as "ur_kinematics"
from .ur5e_ikfast import *  # or ur10e_ikfast, depending on your robot

# Provide a standard name
import sys
sys.modules[__name__ + ".ur_kinematics"] = sys.modules[__name__ + ".ur5e_ikfast"]
