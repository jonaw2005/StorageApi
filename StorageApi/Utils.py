from StorageApi import Item


def toItem(self, x: int, y: int, desc, amount: int):
    item = Item.Item(x, y, desc, amount)
    return item


def itemListToPythonList(itemlist):
    return 0;
