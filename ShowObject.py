import random
import tvdb_api

tvApi = tvdb_api
shows = tvApi.Tvdb()

class Show:
    def __init__(self, showName):
        try:
            self.show = shows[showName]
            self.numSeasons = 0
            for season in self.show:
                if season > 0:
                    self.numSeasons += 1
        except tvApi.tvdb_shownotfound as error:
            raise

    def getNumSeasons(self):
        return self.numSeasons

    def findNumEpisodes(self, Season):
        numEpisodes = 0
        for episode in self.show[Season]:
            numEpisodes += 1
        return numEpisodes

    def seasonGenerator(self):
        return randIntGen(self.getNumSeasons())

    def episodeGenerator(self, Season):
        return randIntGen(self.findNumEpisodes(Season))

    def generateRandomEpisode(self):
        season = self.seasonGenerator()
        episode = self.episodeGenerator(season)
        return (season, episode)

    def printRandomEpisode(self):
        result = self.generateRandomEpisode()
        print("The Random Generator says:")
        print("Season {} Episode {} of {}".format(result[0], result[1], self.show['seriesName']))

def randIntGen(upperBound):
     return random.randint(1, upperBound)
