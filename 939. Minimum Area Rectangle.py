class Solution(object):
    import collections
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ys = collections.defaultdict(list)
        for x, y in points:
            ys[x].append(y)
        d ={}
        area = float('inf')
        for x in sorted(ys):
            ay = ys[x]
            ay.sort()
            for i, y2 in enumerate(ay):
                for j in range(i):
                    y1 = ay[j]
                    # print(x, i,j, y1,y2)
                    if (y1,y2) in d:
                        area = min(area, (x-d[(y1,y2)])*(y2-y1))
                    d[(y1,y2)]=x
        return area if area < float('inf') else 0
            