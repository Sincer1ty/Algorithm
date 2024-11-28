wallet = list(map(int, input().split()))
bill = list(map(int, input().split()))

def solution(wallet, bill):
    answer = 0

    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1

    return answer

print(solution(wallet, bill))