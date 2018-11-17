import random
class Player():

    def __init__(self, name, bane):
        self.pos = 0
        self.omgange = 0
        self.taare = 0
        self.gear = 3
        self.STALIN = False
        self.først = False
        self.sidst = False
        self.name = str(name)
        self.turns = bane


    def __str__(self):
        return "Player nr: {}".format(self.name)

    def getPos(self):
        return  (self.pos + self.omgange * len(self.turns))


    def setFørst(self, val):
        self.først = val
        return

    def setSidst(self, val):
        self.sidst = val
        return


    def roll(self):
        dice = 0
        if self.gear > 3:
            self.gear = 3

        elif self.gear < 1:
            self.gear = 1

        for i in range(self.gear):
            dice += random.randint(1,4)
        return dice

    def af_banen(self, roll):
        self.taare += 12
        self.gear = 1
        self.afbanen = True

        for i in range(roll):
            self.pos+=1
            if self.pos == len(self.turns):
                self.omgange += 1
                self.pos = 0
            if self.turns[self.pos] == 1:
                return


    def take_turn(self):
        temp = self.taare

        self.gear +=1 if self.STALIN

        roll = self.roll()

        if roll >= 10:
            #print("AF BANEN")
            self.af_banen(roll)
            return

        if self.gear == 3 and roll == 3:
            #print("Smadret gearkase")
            self.taare += 12
            self.gear = 1
            return

        else:
            for i in range(roll):
                self.pos+=1
                if self.pos == len(self.turns):

                    self.omgange += 1
                    self.pos = 0

                if roll >= 7 and self.turns[self.pos] == 1:
                    self.taare += 1

        if self.taare ==  temp:
            self.taare += 1
