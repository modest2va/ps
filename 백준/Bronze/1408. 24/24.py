def sol(start_time , end_time):
    start_hh, start_mm, start_ss = map(int, start_time.split(':'))
    end_hh, end_mm, end_ss = map(int, end_time.split(':'))

    total_time = (end_hh-start_hh) * 60 * 60 + (end_mm-start_mm)*60 + end_ss-start_ss
    if total_time<0:
        total_time+=60*60*24
    total_hh = int(total_time/3600)
    total_mm = int( (total_time%3600)/60)
    total_ss = (total_time%3600)%60

    return '%.2d:%.2d:%.2d'%(total_hh, total_mm, total_ss)

if __name__ == '__main__':
    start_time = input()
    end_time = input()
    print(sol(start_time,end_time))