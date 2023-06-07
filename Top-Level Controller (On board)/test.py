import time
from HangulDictionary import Hangul 
from HangulDivider import HangulDivider
import serial

Hangul = Hangul()
Divider = HangulDivider()

global loopRun

RunTime = 0
inputString = ""
Fontsize = 35
    
while True:
    startTime = time.time()
    print("Penplotter로 출력할 글씨를 입력해주세요 >> ")
    inputString = input()
    DividedHangul = Divider.Korean_String_Separater(inputString)
    print(DividedHangul)
    TrajectoryList = Hangul.TrajectoryMaker(Fontsize, DividedHangul)
    Hangul.stringShower(Fontsize, len(DividedHangul), TrajectoryList)
    print("\nGenerated Trajectory: ")
    print(TrajectoryList)
    endTime = time.time()
    samplingTime = endTime - startTime
    RunTime = RunTime + samplingTime
    