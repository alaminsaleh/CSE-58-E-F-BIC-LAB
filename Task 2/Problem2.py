def frequent_words(text, k):
    freq={}
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    max_count = max(freq.values())
    result = []
    for pattern in freq:
        if freq[pattern]==max_count:
            result.append(pattern)
    return result
text="ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
print(" ".joint(frequent_words(text,)))
