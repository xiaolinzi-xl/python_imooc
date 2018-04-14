def numberOfBoomerangs(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(0,len(points)):
            nums_dict = {}
            for j in range(0,len(points)):
                if i != j:
                    dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    if dis in nums_dict:
                        nums_dict[dis] += 1
                    else:
                        nums_dict[dis] = 1
            for value in list(nums_dict.values()):
                ans += value * (value - 1)
        return ans

points = [[0,0],[1,0],[2,0]]
ans = numberOfBoomerangs(points)
print(ans)