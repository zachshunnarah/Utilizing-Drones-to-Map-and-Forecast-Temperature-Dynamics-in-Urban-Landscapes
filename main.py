# IMPORTS
from PIL import Image
import numpy as np
import sys
from thermal_base import ThermalImage

np.set_printoptions(threshold=sys.maxsize)

# ---- BELOW: thermal_base package from github page
def gettemp(image_path):
    image = ThermalImage(image_path=image_path, camera_manufacturer="dji")

    thermal_np = image.thermal_np           # The temperature matrix as a np array
    raw_sensor_np = image.raw_sensor_np     # The raw thermal sensor excitation values as a np array
    meta = image.meta                       # Any other metadata that exiftool picked up

    return thermal_np

#SAVING IMAGES AS TIF FILES... SHOULD GET WHITE IMAGE --- WILL BE SAVED UNDER PYCHARM PROJECTS FOLDER
#EXAMPLE CODE OF WHERE PICTURES WERE LOCATED
temps = gettemp(r"C:\Users\zrshu\OneDrive - College of Charleston\Drone Data Collection\2023_2024\01292024-90morning\DJI_0912_T.JPG")
im = Image.fromarray(temps)
im.save('DJI_0912_T.tif')

