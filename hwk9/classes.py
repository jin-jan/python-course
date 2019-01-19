class Vehicle:
    def __init__(self):
        self.make = "None"
        self.model = "None"
        self.year = 0
        self.weight = 0
        self.needs_maintenance = False
        self.trips_since_maintenance = 0

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_weight(self, weight):
        self.weight = weight

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def repair(self):
        self.needs_maintenance = False
        self.trips_since_maintenance = 0


class Cars(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.is_driving = None

    def drive(self):
        self.is_driving = True
        self.trips_since_maintenance += 1
        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True

    def stop(self):
        self.is_driving = False


class Planes(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.is_flying = None
        if self.trips_since_maintenance == 0:
            self.needs_maintenance = False

    def fly(self):
        if self.needs_maintenance:
            print("Can't Fly until it's repaired")
            return False
        self.is_flying = True
        self.trips_since_maintenance += 1
        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True

    def land(self):
        self.is_flying = False


def main():
    car_1 = Cars()
    car_2 = Cars()
    car_3 = Cars()

    car_1.set_make("make1")
    car_1.set_model("cx5")
    car_1.set_year(2012)
    car_1.set_weight(100)

    car_2.set_make("make2")
    car_2.set_model("tahoe")
    car_2.set_year(2015)
    car_2.set_weight(120)

    car_3.set_make("make3")
    car_3.set_model("jeep")
    car_3.set_year(2019)
    car_3.set_weight(130)

    trip_1 = 50
    trip_2 = 100
    trip_3 = 150

    for _ in range(trip_1):
        car_1.drive()
        car_1.stop()
    info_car_1 = "Make: {}, Model: {}, Year: {}, "\
                 "Weight: {}, NeedsMaintenance: {}, "\
                 "TripsSinceMaintenance: {}\n".format(car_1.get_make(),
                                                      car_1.get_model(),
                                                      car_1.get_year(),
                                                      car_1.get_weight(),
                                                      car_1.needs_maintenance,
                                                      car_1.trips_since_maintenance)
    print(info_car_1, end="")
    for _ in range(trip_2):
        car_2.drive()
        car_2.stop()
    info_car_2 = "Make: {}, Model: {}, Year: {}, "\
                 "Weight: {}, NeedsMaintenance: {}, "\
                 "TripsSinceMaintenance: {}\n".format(car_2.get_make(),
                                                      car_2.get_model(),
                                                      car_2.get_year(),
                                                      car_2.get_weight(),
                                                      car_2.needs_maintenance,
                                                      car_2.trips_since_maintenance)
    print(info_car_2, end="")

    for _ in range(trip_3):
        car_3.drive()
        car_3.stop()
    info_car_3 = "Make: {}, Model: {}, Year: {}, "\
                 "Weight: {}, NeedsMaintenance: {}, "\
                 "TripsSinceMaintenance: {}\n".format(car_3.get_make(),
                                                      car_3.get_model(),
                                                      car_3.get_year(),
                                                      car_3.get_weight(),
                                                      car_3.needs_maintenance,
                                                      car_3.trips_since_maintenance)
    print(info_car_3, end="")

    plane_1 = Planes()
    plane_2 = Planes()
    plane_3 = Planes()

    plane_1.set_make("make1")
    plane_1.set_model("boeing 777")
    plane_1.set_year(2010)
    plane_1.set_weight(40000)

    plane_2.set_make("make2")
    plane_2.set_model("airbus a380")
    plane_2.set_year(2018)
    plane_2.set_weight(400000)

    plane_3.set_make("make3")
    plane_3.set_model("boeing 737")
    plane_3.set_year(2019)
    plane_3.set_weight(4000000)

    for _ in range(trip_1):
        plane_1.fly()
        plane_1.land()

    info_plane_1 = "Make: {}, Model: {}, Year: {}, "\
                   "Weight: {}, NeedsMaintenance: {}, "\
                   "TripsSinceMaintenance: {}\n".format(plane_1.get_make(),
                                                        plane_1.get_model(),
                                                        plane_1.get_year(),
                                                        plane_1.get_weight(),
                                                        plane_1.needs_maintenance,
                                                        plane_1.trips_since_maintenance)
    print(info_plane_1, end="")

    for _ in range(trip_2):
        plane_2.fly()
        plane_2.land()

    info_plane_2 = "Make: {}, Model: {}, Year: {}, "\
                   "Weight: {}, NeedsMaintenance: {}, "\
                   "TripsSinceMaintenance: {}\n".format(plane_2.get_make(),
                                                        plane_2.get_model(),
                                                        plane_2.get_year(),
                                                        plane_2.get_weight(),
                                                        plane_2.needs_maintenance,
                                                        plane_2.trips_since_maintenance)
    print(info_plane_2, end="")

    for _ in range(trip_3):
        plane_3.fly()
        plane_3.land()

    info_plane_3 = "Make: {}, Model: {}, Year: {}, " \
                   "Weight: {}, NeedsMaintenance: {}, " \
                   "TripsSinceMaintenance: {}\n".format(plane_3.get_make(),
                                                        plane_3.get_model(),
                                                        plane_3.get_year(),
                                                        plane_3.get_weight(),
                                                        plane_3.needs_maintenance,
                                                        plane_3.trips_since_maintenance)
    print(info_plane_3, end="")


main()
