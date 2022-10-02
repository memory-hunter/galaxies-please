import random

class Document:
    def __init__(self, data, false_data):
        self.name = data["name"]
        self.img = data["img"]
        self.jwtsimage = data["jwstimage"]
        self.distance = data["distance"]
        self.type = data["type"]
        self.size = data["size"]
        self.constellation = data["constellation"]
        self.doctype = data["doctype"]
        self.false_data = false_data
        self.fact = True

    def present(self):
        falsify = random.randint(0, 6)
        if falsify > 3:
            self.falsifyinfo()
        return self

    def falsifyinfo(self):
        falsifyindex = [random.randint(1, 2), random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
                        random.randint(1, 2)]
        amountfalsified = 0

        if falsifyindex[0] == 2 and self.distance != self.false_data["distance"]:
            self.distance = self.false_data["distance"]
            amountfalsified += 1

        if falsifyindex[1] == 2 and self.type != self.false_data["type"]:
            self.type = self.false_data["type"]
            amountfalsified += 1

        if falsifyindex[2] == 2 and self.luminosity != self.false_data["constellation"]:
            self.luminosity = self.false_data["constellation"]
            amountfalsified += 1

        if falsifyindex[3] == 2 and self.size != self.false_data["size"]:
            self.size = self.false_data["size"]
            amountfalsified += 1

        if amountfalsified == 0:
            defran = random.randint(0, 3)
            if defran == 0:
                self.distance = self.false_data["distance"]
            elif defran == 1:
                self.type = self.false_data["type"]
            elif defran == 2:
                self.luminosity = self.false_data["constellation"]
            elif defran == 3:
                self.size = self.false_data["size"]
        self.fact = False

    def to_array(self):
        return [self.name, self.img, self.distance, self.type, self.constellation, self.size, self.doctype, self.fact]
