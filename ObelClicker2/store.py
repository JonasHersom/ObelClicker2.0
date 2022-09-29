class Upgrade:
    def __init__(self, name, price=0, ops=0, opk=-1, multiplier=1.0, add=0):
        self.name = name
        self.price = price
        self.owned = 0

        self.ops = ops
        self.opk = opk

        self.multiplier = multiplier
        self.add = add

class Store:
    def __init__(self):
        """ Storefront class """
        self.items = (
            Upgrade("xhamster", price=10, ops=0.3333, multiplier=1.05),
            Upgrade("lube", price=100, opk=1, add=50),
            Upgrade("obelfans", price=1000, ops=25, multiplier=1.01),
        )
        self.balance = 0

    def get(self, item: str):
        """ Get an upgrade from name """
        for i in self.items:
            if i.name == item:
                return i

    def buy(self, item: str):
        """ Buy a specific item """
        itm = self.get(item)
        
        if itm is None:
            return False

        if itm.price > self.balance:
            return False

        self.balance -= itm.price
        itm.owned += 1
        itm.price *= itm.multiplier
        itm.price += itm.add

        return True

    def ops(self):
        """ Get the amount of ops (obel per sekund) the store produces """
        ops = 0
        for i in self.items:
            ops += i.owned * i.ops

        return ops

    def opk(self):
        """ Get the amount of opk  (obel per klik) the store produces """
        opk = 1
        for i in self.items:
            if i.opk != -1:
                opk += i.owned * i.opk

        return opk

        



