class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # dic = {}
        # for i in range(len(s)):
        #     if s[i] in dic and dic[s[i]] != t[i]:
        #         return False
        #     if s[i] not in dic:
        #         dic[s[i]] = t[i]
        # return True
    
        # 위의 코드로 처리하면 한 쪽 방향만 검사하므로 불완전함. 두 개의 문자가 한 문자에 대응하는 경우를 걸러내지 못하기 때문. 
        map_s_t, map_t_s = {}, {}
        for i in range(len(s)):
            if s[i] in map_s_t:
                if map_s_t[s[i]] != t[i]:
                    return False
            else:
                map_s_t[s[i]] = t[i]
            if t[i] in map_t_s:
                if map_t_s[t[i]] != s[i]:
                    return False
            else:
                map_t_s[t[i]] = s[i]
        return True