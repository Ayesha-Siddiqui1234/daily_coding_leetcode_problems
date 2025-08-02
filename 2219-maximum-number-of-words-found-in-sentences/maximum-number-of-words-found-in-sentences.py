class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_count = 0
        for i in range (len(sentences)):
            word = sentences[i].split(" ")
            word_count = max(word_count , len(word));
        return word_count
        