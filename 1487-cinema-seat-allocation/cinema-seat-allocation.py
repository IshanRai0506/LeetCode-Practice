class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        # Rows without any reservation can fit 2 groups
        answer = (n - len(rows)) * 2

        for seats in rows.values():

            # Left block: 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Middle block: 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Right block: 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # Both sides are free
                answer += 2

            elif left or middle or right:
                # At least one group can fit
                answer += 1

        return answer