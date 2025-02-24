def sol(nums):

        return True

if __name__ == '__main__':
    start_hh, start_mm, start_ss =map(int,input().split(':'))
    end_hh, end_mm, end_ss = map(int, input().split(':'))
    start_total = start_hh*3600 + start_mm*60 + start_ss
    end_total = end_hh*3600 + end_mm*60 + end_ss
    answer = end_total-start_total
    if end_total<start_total:
         answer+= 24*3600
    print(answer)