class IceCream:
      def __init__(self, flavor, scoops, container):
            self.flavor = flavor
            self.scoops = scoops
            self.container = container
            
      def serve(self):
            print("Serving " + str(self.scoops) + " scoops of " + self.flavor + " ice cream in a " + self.container + ".")


class ConeIceCream(IceCream):
            def __init__(self):
            #To assign specific values to attributes using super()
                  super().__init__(flavor = "Vanilla", scoops = 2, container = "cone")


class CupIceCream(IceCream):
      def __init__(self):
            super().__init__(flavor = "Chocolate", scoops = 3, container = "cup")

cone = ConeIceCream()
cup = CupIceCream()
ice_cream = [ConeIceCream, CupIceCream]

for icecream in ice_cream:
      icecream.serve(self)
