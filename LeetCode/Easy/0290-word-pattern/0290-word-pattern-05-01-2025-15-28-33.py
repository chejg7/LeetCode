class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_p_s, map_s_p = {}, {}
        s_list = s.split(' ')

        if len(pattern) != len(s_list):
            return False


        for i in range(len(pattern)):
            if pattern[i] in map_p_s:
                if map_p_s[pattern[i]] != s_list[i]:
                    return False
            else:
                map_p_s[pattern[i]] = s_list[i]
            if s_list[i] in map_s_p:
                if map_s_p[s_list[i]] != pattern[i]:
                    return False
            else:
                map_s_p[s_list[i]] = pattern[i]
        
        return True