from random import randint


class Auto:
    material = 'steel'
    secret_model_id = 12345

    def __init__(self, color, engine_power):
        self.color = color
        self.engine_power = engine_power
        self.is_on = False
        self.secret_number = randint(0, 100_000_000)

    def gas(self):
        if not self.is_on:
            print("You have to switch on your car!")
            return
        print(f"Auto with color {self.color} and material {Auto.material} and engine power"
              f" {self.engine_power} make Wruuuuuuummmmmmm")

    def switch_on(self):
        if self.is_on:
            print("Auto has been switched on yet!")
            return
        self.is_on = True

    def switch_off(self):
        if not self.is_on:
            print("Auto has been switched off yet!")
            return
        self.is_on = False

    def info(self):
        print(f"{self.color}, {self.engine_power}")


class WarAuto(Auto):
    def __init__(self, color, engine_power, weapon_type):
        super().__init__(color, engine_power)
        self.weapon_type = weapon_type

    def shoot(self):
        print("Fire!!!!")

    def gas(self):
        super().gas()
        print("I make noise by my machinegun!")


class MedicineAuto(Auto):
    def heal_somebody(self):
        print("heal!")

    def gas(self):
        super().gas()
        print("I AM HEAL MACHINE!")


class MedWarCar(WarAuto, MedicineAuto):
    pass


# my_shiny_auto = Auto('red', 100)
# my_shiny_auto2 = Auto('blue', 200)
# my_shiny_auto3 = Auto('black', 300)
# print(Auto.material)
# print(my_shiny_auto.material)
# print(Auto._Auto__secret_model_id)
# my_shiny_auto.gas()
# my_shiny_auto2.gas()
# my_shiny_auto3.gas()
# print(my_shiny_auto.__is_on)
# my_shiny_auto.switch_on()
# my_shiny_auto.switch_on()
# print(my_shiny_auto.is_on)
war_car = WarAuto('red', 100, 'pistol')
med_war_car = MedWarCar('red', 100, 'pistol')
# med_war_car.heal_somebody()
med_war_car.gas()
# medicine_car = MedicineAuto('red', 100)
# war_car.switch_on()
# medicine_car.switch_on()
# war_car.shoot()
# war_car.gas()
