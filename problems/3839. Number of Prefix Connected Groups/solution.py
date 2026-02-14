class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        words.sort()
        groups_count = 0
        group_members_count = 0
        prev_prefix = "_"
        for word in words:
            if len(word) < k:
                print("skipped : ", word)
                continue;
            current_prefix = word[0:k]
            if current_prefix == prev_prefix:
                group_members_count += 1
            else:
                if group_members_count >= 2:
                    groups_count += 1
                prev_prefix = current_prefix
                group_members_count = 1
            print(word, group_members_count, groups_count)
        if group_members_count >= 2:
            groups_count += 1
        return groups_count