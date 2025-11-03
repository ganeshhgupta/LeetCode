class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        # O(F × L), O(U × L)

        lang_map = defaultdict(set)

        for i, lang_list in enumerate(languages, 1):  # user indices start at 1
            lang_map[i] = set(lang_list)

        sad_users = set()

        for u, v in friendships:
            if lang_map[u].intersection(lang_map[v]):
                continue
            sad_users.add(u)
            sad_users.add(v)

        lang_count = defaultdict(int)
        for user in sad_users:
            for lang in lang_map[user]:
                lang_count[lang] += 1

        return len(sad_users) - max(lang_count.values(), default=0)
