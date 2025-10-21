from .update_strategy import UpdateStrategy

class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
            return

        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1
