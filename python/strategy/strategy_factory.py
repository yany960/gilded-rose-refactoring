from .normal_item_strategy import NormalItemStrategy
from .aged_brie_strategy import AgedBrieStrategy
from .backstage_pass_strategy import BackstagePassStrategy
from .sulfuras_strategy import SulfurasStrategy
from .conjured_strategy import ConjuredStrategy

class StrategyFactory:
    @staticmethod
    def get_strategy(item):
        if "Aged Brie" in item.name:
            return AgedBrieStrategy()
        elif "Backstage" in item.name:
            return BackstagePassStrategy()
        elif "Sulfuras" in item.name:
            return SulfurasStrategy()
        elif "Conjured" in item.name:
            return ConjuredStrategy()
        else:
            return NormalItemStrategy()
