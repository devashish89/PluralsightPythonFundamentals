from contextlib import closing

class Refrigerator_Raid:

    def open(self):
        print("Open fridge door")

    def take(self, food):
        if (food == "Pizza"):
            raise RuntimeError("Unhealthy food!")
        print("Taking {}".format(food))

    def close(self):
        print('Close fridge door')


# def raid(food):
#     r = Refrigerator_Raid()
#     r.open()
#     r.take(food)
#     r.close()

def raid(food):
    with closing(Refrigerator_Raid()) as f:
        f.open()
        f.take(food)