class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_letters = list(ransomNote)
        m_letters = list(magazine)
        for r in r_letters:
            if r not in m_letters:
                return False
            m_letters.remove(r)
        return True