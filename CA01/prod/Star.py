'''
Created on Feb 22, 2016

@author: nopenshaw
'''

class Star:
    '''
    classdocs
    '''


    def __init__(self, starId, magnitude, rightAscension, declination):
        '''
        Constructor
        '''
        self.starId = starId
        self.magnitude = magnitude
        self.rightAscension = rightAscension
        self.declination = declination
        pass
        
    def getStarId(self):
        return self.starId
    
    def getMagnitude(self):
        return self.magnitude
    
    def getRightAscension(self):
        return self.rightAscension
    
    def getDeclination(self):
        return self.declination
    
    def toString(self):
        output = str(self.starId), str(self.magnitude), str(self.rightAscension), str(self.declination)
        return output
    