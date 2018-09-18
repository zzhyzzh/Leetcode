class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashMap = {}
        for i, name in enumerate(list1):
            hashMap[name] = i
        minSum = 2001
        minSet = []
        for i, name in enumerate(list2):
            if name in hashMap:
                if i + hashMap[name] < minSum:
                    minSum = i + hashMap[name]
                    minSet = [name]
                    continue
                if i + hashMap[name] == minSum:
                    minSet.append(name)
                    continue

        return minSet

solution = Solution()
result = solution.findRestaurant(
["Shogun", "Tapioca Express", "Burger King", "KFC"],
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
print(result)
print(type(result))
