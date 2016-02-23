from Star import Star
#import math
#import struct

class StarCatalog:
    
    def __init__(self):
    
        self.starList = list()
        self.starCount = 0
        pass
    
    def loadCatalog(self, starFile=None, Magnitude=6.0):
        #Check for valid parameters
        if (len(starFile) < 1):
            raise ValueError("Cannot load empty filename. Exiting.")
        elif (Magnitude > 30 or Magnitude < -30):
            raise ValueError("Error, Magnitude out of range. |-30 <= Magnitude <= 30|")   
        else:
            #Try to open file, throw exception if there's an error.
            try:
                fileId = open(starFile, 'r')
            except ValueError:
                print "Unable to open file. Exiting."
                
            #CONTINUE WITH READING IN FILE DATA
            #SAO is StarId                -> bits 1 - 6
            #Vmag is Magnitude            -> bits 81 - 84
            #RAJ2000 is Right Ascension   -> bits 184 - 193
            #DEJ2000 is Declination       -> bits 194 - 204
            starIdList = list()
            currentLine = 0
            loopCount = 0
            while(fileId.next() and loopCount < 300000):
            #while(currentLine <= 10):
                
                fileId.seek(currentLine*205 + 0,0)
                tempId = str(fileId.read(6))
                fileId.seek(currentLine*205 + 80,0)
                tempMag = float(str(fileId.read(4)))
                fileId.seek(currentLine*205 + 182,0)
                tempRA = float(str(fileId.read(10)))
                #tempRAf = struct.unpack('f', tempRA) --> Tried to convert to degrees
                #math.degrees(tempRAf)
                fileId.seek(currentLine*205 + 192,0)
                tempDE = str(fileId.read(11))
                #tempDEf = struct.unpack('f',tempDE) --> Tried to convert to degrees
                #math.degrees(tempDEf)
                currentLine += 1
            
                tempStar = Star(tempId, tempMag, tempRA, tempDE)
                #print tempStar.toString()
                
                #Make sure all conditions of Temp Star will be accepted in the Star Catalogue per the spec
                #Will check ID, Vmag, Right Ascension, and Declination
                if(tempStar.magnitude <= Magnitude and tempStar.magnitude >= -30 and tempStar.starId not in starIdList):
                    self.starList.append(tempStar)
                    self.starCount += 1
                    starIdList.append(tempId)
                    #print "Adding: ", tempStar.toString()
            #infinite loop breaker
                loopCount += 1
        pass
    
    def emptyCatalog(self):
        #Popping items from the list as you go
        count = 0
        while (self.starCount > 0):
            #print "Popping loop"
            #print self.starList.pop().getStarId()
            self.starCount -= 1
            count += 1
        return count
    
        pass
    
    def getStarCount(self, dimmest=30.0, brightest=-30.0):
        #Check to see that the dimmest and brightest parameters agree with spec
        if ((dimmest > 30.0 or dimmest < -30.0) or (brightest > 30.0 or brightest < -30.0) or (brightest > dimmest)):
            raise ValueError("Error. Dimmest and brightest values must be between -30 and 30. Dimmest must be greater than brightest.")
        #Count Stars
        else:
            count = 0
            for star in self.starList:
                if (star.getMagnitude() <= dimmest and star.getMagnitude() >= brightest):
                    count += 1
            return count
        pass
    
    def getStarData(self, starId):
        #Check if blank starId was given
        if (len(starId) < 1):
            raise ValueError("Error. Cannot find star with no name.")
        #Check if a non string was passed
        elif (type(starId) is not str):
            raise ValueError("Error. StarId must be a string.")   
        #Try to find a Star in the List with matching ID, if not, throw Value Error exception
        else:
            try:
                pos = 0
                for star in self.starList:
                    if (star.getStarId() == starId):
                        starLoc = pos
                        starData = self.starList[starLoc]
                        print "Found Star Data: ",starData,"."
                        if (star.getMagnitude() < -30 or star.getMagnitude() > 30 or type(star.getMagnitude()) is not int or star.getRightAscension() < 0 or star.getRightAscension() >= 360 or type(star.getRightAscension()) is not int or star.getDeclination() < -90 or star.getDeclination() > 90 or type(star.getDeclination()) is not int):
                            raise ValueError("Error. Star has attributes out of bounds.")
                        else:
                            return starData
                    pos += 1
            except ValueError:
                print "Error. Unable to find star."
        pass