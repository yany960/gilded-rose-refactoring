# -*- coding: utf-8 -*-
from strategy.strategy_factory import StrategyFactory

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = StrategyFactory.get_strategy(item)
            strategy.update(item)