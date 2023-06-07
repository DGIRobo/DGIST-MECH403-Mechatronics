import time
from HangulDictionary import Hangul 
from HangulDivider import HangulDivider
import serial

Hangul = Hangul()
Divider = HangulDivider()
s = serial.Serial('COM4', 115200)
z_offset = 13

def Trajectory2Gcode(trajectory):
    for dotIndex in range(len(trajectory)):
        trajectory[dotIndex] = f"G90 X{round(trajectory[dotIndex][0], 4)} Y{round(5/6*trajectory[dotIndex][1], 4)} Z{1-z_offset*float(trajectory[dotIndex][2])}"
    return trajectory

global loopRun

Event = 0
RunTime = 0
inputString = ""
Fontsize = 0
numlist = []

while True:
    inputString = None
    DividedHangul = None
    TrajectoryList = None
    Gcode = None
    startTime = time.time()
    print("Penplotter로 출력할 글씨의 크기를 입력해주세요 >>")
    Fontsize = int(input())
    print("Penplotter로 출력할 글씨를 입력해주세요 >> ")
    inputString = input()
    DividedHangul = Divider.Korean_String_Separater(inputString)
    TrajectoryList = Hangul.TrajectoryMaker(Fontsize, DividedHangul)
    #Hangul.stringShower(Fontsize, len(DividedHangul), TrajectoryList)
    Gcode = Trajectory2Gcode(TrajectoryList)
    print(Gcode)
    
    if Event == 0:
        s.write(('F500' + '\n').encode())
        s.write(('G21' + '\n').encode())
        s.write(('$100 = 5' + '\n').encode()) # x offset 5step = 1mm for y-axis
        s.write(('$101 = 5' + '\n').encode()) # y offset 5step = 1mm for y-axis
        s.write(('$102 = 10' + '\n').encode()) # z offset 5step = 1mm for y-axis
        s.write(('G92 X0 Y0' + '\n').encode())
        s.write(('G04 p0.5\n').encode())
    Event = Event + 1
    
    for dotIndex in range(len(Gcode)):
        s.write((Gcode[dotIndex] + '\n').encode())
        print('Sending: ' + Gcode[dotIndex])
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print(' : ' + grbl_out.strip().decode())
        print('Sending: G04 p0.5\n')
        s.write(('G04 p0.5\n').encode())
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print(' : ' + grbl_out.strip().decode())
    s.write(('G92 X0 Y0' + '\n').encode())
    
    print(len(Gcode))
    endTime = time.time()
    samplingTime = endTime - startTime
    RunTime = RunTime + samplingTime
    
    