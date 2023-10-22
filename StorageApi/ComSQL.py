from StorageApi import Utils


class ComSQL:

    def __int__(self):
        # init database
        pass

    def makeString(self):
        pass

    def makeRequest(self):
        pass

    def getAllItems(self):
        # return as list like json
        # get all items
        pass

    def getItem(self, x, y):
        list = self.makeRequest()
        item = Utils.toItem(list)
        return item

    def putItem(self, item):
        pass

    def status(self):
        return "active"
