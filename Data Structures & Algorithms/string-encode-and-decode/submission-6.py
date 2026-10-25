class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        if len(strs)==0:
            return "…"
        if len(strs)==1:
            return strs[0]
        for str_ in strs:
            encoded += str_
            encoded += "¬"
        encoded = encoded[:-1]
        return encoded
    def decode(self, s: str) -> List[str]:
        if s == "…":
            return []
        if "¬" not in s:
            return [s]
        return s.split("¬")