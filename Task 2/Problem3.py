pattern = "AAAACCCGGT"
comp = {'A':'T','T':'A','C':'G','G':'C'}
result = ""
for ch in pattern:
    result = comp[ch] + result
print(result)
