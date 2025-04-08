class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return float(0)
        
        output: float = 0
        prev_upper, prev_percent = 0, 0

        for bracket in brackets:
            upper, percent = bracket

            if income > upper:
                output += (upper - prev_upper) * percent

            if income <= upper:
                output += (income - prev_upper) * percent
                break

            prev_upper, prev_percent = upper, percent

        return output / 100