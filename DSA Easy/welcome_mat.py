#My solution for Welcome mat
n, m = input().split()
N=int(n)
M=int(m)
a='-'
b='.|.'

for i in range(int(N/2)):
    print((b*i).rjust((M-3)//2,a)+b+(b*i).ljust((M-3)//2,a))
    
print('WELCOME'.center(M,'-'))

for i in range(int(N/2)):
    print((b*(int(N/2)-i-1)).rjust((M-3)//2,a)+b+(b*(int(N/2)-i-1)).ljust((M-3)//2,a))
