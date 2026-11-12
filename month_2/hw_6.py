prices = [
   100, 120, 135, 150, 175, 190, 200, 215,
   230, 250, 275, 290, 300, 320, 340, 350,
   370, 390, 400, 420, 440, 450, 470, 490,
   500, 520, 540, 560, 580, 600, 620, 650,
   670, 690, 700, 720, 740, 760, 780, 800,
   820, 850, 870, 890, 900, 920, 950, 980,
   1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400,
   1500, 1600, 1750, 1800, 2000, 2200, 2500, 3000
]

class SearchEngine:
    def __init__(self, prices):
        self.prices = prices

    def linear_search(self, target):
        for index, price in enumerate(self.prices):
            if price == target:
                return index
        return -1

    def binary_search(self, target):
        left, right = 0, len(self.prices) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.prices[mid] == target:
                return mid
            elif self.prices[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


search_engine = SearchEngine(prices)



index_300 = search_engine.linear_search(300)
index_450 = search_engine.binary_search(450)
index_500 = search_engine.binary_search(500)

print(f"Индекс цены 300: {index_300}")
print(f"Индекс цены 450: {index_450}")
print(f"Индекс цены 500: {index_500}")