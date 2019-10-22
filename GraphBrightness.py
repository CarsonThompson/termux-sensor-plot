import sys
import subprocess
import json
import shlex
import time
import matplotlib.pyplot as plot

import GraphPoints

delayms = "50"

log = False
startTime = time.time()
currentTime = 0

lenFound = False
JSONlength = 1
                   
if len(sys.argv) == 3 :
    if sys.argv[1] == "-l" :
        logFile = open(sys.argv[2],"w")
        log = True
        
BrightnessJSON = subprocess.Popen(shlex.split(
             "termux-sensor -d" + delayms + " -s light"),
             stdout=subprocess.PIPE)

try:
    while True:
        currentLine = 0
        currentJSON = ""
    
        while currentLine < JSONlength :
            currentJSON += BrightnessJSON.stdout.readline().decode("utf-8")
            currentLine += 1
        
            if lenFound == False:
                try: 
                    json.loads(currentJSON)
                except:
                    JSONlength += 1
                else:
                    lenFound = True

    
        currentBrightness = (json.loads(currentJSON)
                        ["TMD2725 Ambient Light"]["values"][0])

        print (currentBrightness)
        
        if log == True :
            currentTime = time.time() - startTime
        
            logFile.write(str(currentTime) + ", " +
                       str(currentBrightness) + "\n")

except KeyboardInterrupt :
    logFile.close()
    GraphPoints.exportPlot(sys.argv[2])
    print ("I HAVE YOU!!!")
    