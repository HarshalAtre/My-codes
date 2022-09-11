try:
    a=int(input())
    c=1/a
    print(c)

except:
    print('error')

finally:# PRRINT IRRESPECTIVE OF WHAT HAPPENS IN EXCEPT ,EVEN IF WE EXIT() IT STILL RUNS
    print('WE ARE DONE')






