class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        weakest_rows = []
        for rows in mat:
            for num in rows:
                if num < 1:
                    weakest_rows.append()
                for k in range(k):
                    rows = f"{k}"


Solution.kWeakestRows(
    Solution,
    [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    3,
)
