
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDays(date):
            month = int(date[:2])
            day = int(date[3:])
            
            return sum(months[:month - 1]) + day

        start = max(getDays(arriveAlice), getDays(arriveBob))
        end = min(getDays(leaveAlice), getDays(leaveBob))

        return max(0, end - start + 1)