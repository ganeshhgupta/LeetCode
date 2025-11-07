class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Calculate initial power for each city using sliding window
        power = [0] * n
        window_sum = 0
        
        # Initial window for city 0
        for i in range(min(n, r + 1)):
            window_sum += stations[i]
        power[0] = window_sum
        
        # Slide window for remaining cities
        for i in range(1, n):
            # Add right element if exists
            if i + r < n:
                window_sum += stations[i + r]
            # Remove left element if exists
            if i - r - 1 >= 0:
                window_sum -= stations[i - r - 1]
            power[i] = window_sum
        
        def canAchieve(min_power):
            added = [0] * n  # Additional stations at each position
            used = 0
            total = 0  # Current power using sliding window
            
            # Initialize window for city 0
            for i in range(min(n, r + 1)):
                total += stations[i] + added[i]
            
            for i in range(n):
                # Update sliding window if not first city
                if i > 0:
                    if i + r < n:
                        total += stations[i + r] + added[i + r]
                    if i - r - 1 >= 0:
                        total -= stations[i - r - 1] + added[i - r - 1]
                
                # Check if current city needs more power
                if total < min_power:
                    need = min_power - total
                    used += need
                    
                    if used > k:
                        return False
                    
                    # Add stations at rightmost position in range
                    pos = min(n - 1, i + r)
                    added[pos] += need
                    total += need  # Update current total
            
            return True
        
        # Binary search
        left, right = min(power), min(power) + k
        
        while left < right:
            mid = (left + right + 1) // 2
            if canAchieve(mid):
                left = mid
            else:
                right = mid - 1
        
        return left