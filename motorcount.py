# Explorer Hat test of interrupts using Python
# Pins 
# Brown - GND
# Red - A timing
# Tan - Motor 2
# Yellow - B Timing
# Green - VCC 5V
# Blue - Motor 1

import time, sys
import explorerhat as eh

count = 0
rotations = 0

def changed(input):
  global count, rotations
  count = count + 1
  if(count > 22):
     rotations = rotations + 1 
     print("Rotations: {} Count:{}".format(rotations,count))
     count = 0

def main(argv):
   eh.input.one.changed(changed)

   eh.motor.one.forwards(int(argv[1]))
   print("Starting motor, speed:{}",format(argv[1]))

   print("Sleeping")
   time.sleep(10)

   print("Add Done!")
   eh.motor.one.forwards(0)

if __name__ == "__main__":
    main(sys.argv)



