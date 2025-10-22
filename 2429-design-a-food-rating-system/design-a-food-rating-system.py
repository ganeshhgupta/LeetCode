class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rate_map = {}             # food -> rating
        self.food_to_cuisine = {}      # food -> cuisine
        self.cuisine_heap = defaultdict(list)  # cuisine -> [(-rating, name)]

        for f, c, r in zip(foods, cuisines, ratings):
            self.rate_map[f] = r
            self.food_to_cuisine[f] = c
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.rate_map[food] = newRating
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]

        while heap:
            rating, food = heap[0]
            if -rating == self.rate_map[food]:
                return food
            heapq.heappop(heap)
