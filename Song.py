class Song:
    confidence = {}
    title = ""

    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def getConfidence(self):
        return self.confidence
    
    def getGenres(self):
        # run this song through model to get genre confidence values, set in dictionary
        pass