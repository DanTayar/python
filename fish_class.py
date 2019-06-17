class Fish(Animal):

    def __init__(self, fines,scales,color,weight,lenght):
        self.fines = fines
        self.scales = scales
        self.color = color
        self.weight = weight
        self.lenght = lenght

    def print_out_details(self):
        print(self.fines,"fines")
        print(self.scales," scales")
        print("color",self.color)

class kosher_fish(Fish):

    #if you dont use the init here then it will use the init from the fish


    def __init__(self, fines,scales,color,weight,lenght):
        self.fines = True
        self.scales = True
        self.color = color
        self.weight = weight
        self.lenght = lenght

    shark = Fish(True,False,1000,80,"grey")
    shark.print_out_details()

    salmon = kosher_fish(True,False,5,10,"pink")
    salmon.print_out_details()