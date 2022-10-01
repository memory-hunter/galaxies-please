import random


class Document:
    def __init__(self, data, false_data):
        self.name = data["name"]
        self.img = data["img"]
        self.distance = data["distance"]
        self.type = data["type"]
        self.luminosity = data["luminosity"]
        self.size = data["size"]
        self.doctype = data["doctype"]
        self.false_data = false_data
        self.fact = True

    def present(self):
        falsefy = random.randint(0, 6)
        if falsefy > 3:
            self.falsifyinfo()
        return self

    def falsifyinfo(self):
        # 0-img, 1-distance, 2-type, 3-luminosity, 4-size
        falsifyindex = [random.randint(1, 2), random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
                        random.randint(1, 2)]
        amountfalsified = 0

        if falsifyindex[0] == 2:
            self.img = self.false_data["img"]
            amountfalsified += 1

        if falsifyindex[1] == 2 and self.distance != self.false_data["distance"]:
            self.distance = self.false_data["distance"]
            amountfalsified += 1

        if falsifyindex[2] == 2 and self.type != self.false_data["type"]:
            self.type = self.false_data["type"]
            amountfalsified += 1

        if falsifyindex[3] == 2 and self.luminosity != self.false_data["luminosity"]:
            self.luminosity = self.false_data["luminosity"]
            amountfalsified += 1

        if falsifyindex[4] == 2 and self.size != self.false_data["size"]:
            self.size = self.false_data["size"]
            amountfalsified += 1

        if amountfalsified == 0:
            defran = random.randint(0,4)
            if defran == 0:
                self.img = self.false_data["img"]
            elif defran == 1:
                self.distance = self.false_data["distance"]
            elif defran == 2:
                self.type = self.false_data["type"]
            elif defran == 3:
                self.luminosity = self.false_data["luminosity"]
            elif defran == 4:
                self.size = self.false_data["size"]
        self.fact = False

    def arrayfy(self):
        return [self.name, self.img, self.distance, self.type, self.luminosity, self.size, self.doctype, self.fact]
