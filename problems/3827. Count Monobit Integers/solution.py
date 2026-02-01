class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        for i in range(1, n+1):
            print(str(bin(i))[2:])
            if '0' not in str(bin(i))[2:]:
                print("yes")
                count += 1

        return count