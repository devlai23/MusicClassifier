class Song:
    confidence = {}
    title = ""

    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def getConfidence(self):
        return self.confidence
    
    # confidence should be of the form ("percent confidence (ie. 0.9) : genre (ie Classical")
    def setConfidence(self, dict):
        confidence = dict