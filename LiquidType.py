from enum import Enum

class LiquidType(Enum):
    WATER = "Water"
    ISOPROPANOL = "Isopropanol"
    ETHANOL = "Ethanol"
    METHANOL = "Methanol"
    ACETONE = "Acetone"
    GLYCEROL = "Glycerol"
    OIL = "Oil"
    MERCURY = "Mercury"

    def is_flammable(self):
        flammable_liquids = {"Isopropanol", "Ethanol", "Methanol", "Acetone"}
        return self.value in flammable_liquids

    def is_viscous(self):
        viscous_liquids = {"Glycerol", "Oil"}
        return self.value in viscous_liquids

    def is_safe_for_human_contact(self):
        safe_liquids = {"Water", "Ethanol", "Isopropanol", "Glycerol"}
        return self.value in safe_liquids


