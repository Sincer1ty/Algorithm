def get_common_subsequence(sequences):
    seq1 = sequences[0]
    common_subseq = ""
    
    for length in range(1, len(seq1) + 1):
        for i in range(len(seq1) - length + 1):
            sub = seq1[i:i + length]
            all_found = True
            for seq in sequences:
                if sub not in seq:
                    all_found = False
                    break
            if all_found:
                if len(sub) > len(common_subseq) or (len(sub) == len(common_subseq) and sub < common_subseq):
                    common_subseq = sub
    # return common_subseq if len(common_subseq) >= 3 else "no significant commonalities"
    if len(common_subseq) >= 3:
        return common_subseq
    else:
        return "no significant commonalities" 

N = int(input())
for _ in range(N):
    M = int(input())
    Dna = [input().strip() for _ in range(M)]
    result = get_common_subsequence(Dna)
    print(result)