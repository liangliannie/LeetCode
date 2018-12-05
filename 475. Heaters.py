class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        i,r = 0,0
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')]+ heaters +[float('inf')]
        for house in houses:
            while house > heaters[i+1]:
                i+=1
            dis = min(house - heaters[i], heaters[i+1]-house)
            r = max(dis, r)
        return r