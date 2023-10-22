from StorageApi import ComSQL, ComArduino, Item, Utils


class StorageHandler:
    # every action --> new thread that checks if done
    #    --> done: status=available --> callback to adjust database to new content

    items = []
    #SQLHandler = 0
    #ArduinoHandler = 0

    def __int__(self):
        self.SQLHandler = ComSQL.ComSQL()
        self.ArduinoHandler = ComArduino.ComArduino()


    def allItems(self):
        itemlist = self.SQLHandler.getAllItems()
        data = itemlist
        # TODO: convert to "ITEM" datatype and back or get list directly from db????
        # data = Utils.itemListToPythonList(itemlist)
        return data

    def takeItem(self, x, y):
        item = self.SQLHandler.getItem()

        # TODO: check if item is available

        self.getItemThread(item)
        pass

    def putItem(self, x, y, desc, amount):
        item = Utils.toItem(x, y, desc, amount=amount)

        self.putItemThread(item)

        pass

    def relocateItem(self, prevX, prevY, newX, newY):
        item_old = self.SQLHandler.getItem(prevX, prevY)
        item_new = Utils.toItem(newX, newY, item_old.getDesc(), item_old.getAmount())

        self.relocateItemThread(item_old, item_new)

        # TODO: check if item is available and new pos is free

        # take item --> wait till in reset pos --> put item

        pass

    def resetCrane(self):
        self.ArduinoHandler.reset()

    def checkReady(self):
        pass

    def putItemThread(self, item):
        pass

    def getItemThread(self, item):
        pass

    def relocateItemThread(self, item_old, item_new):
        pass

    def getStatus(self):
        sql_status = self.SQLHandler.status()
        arduino_status = self.ArduinoHandler.status()
        return {'sql': sql_status, 'arduino': arduino_status}
