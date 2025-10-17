def taloy_pol(x,L):#泰勒多项式,x为自变量,L为一列表，存放了[x0,f(x0),...]‘...’表示f的n阶导数
    sum = L[-1]
    for i in range(2,len(L)):
        if i ==len(L):
            sum*=(x-L(0))
            sum+=L[1]
        sum =sum*(x-L[0])/(len(L)-i)
        sum +=L[-i]
    return sum
def newton_pol(im1,im2,im3=None,j=0):   #采用递归实现牛顿多项式系数
    im = []
    if im3 == None:
        im3 = []
    im3.append(im2[0])
    if j==len(im1)-1:
        return im3
    for i in range(1,len(im2)):
        im.append((im2[i]-im2[i-1])/(im1[i+j]-im1[i-1])) #用循环求得表格的第2+n列（n为递归的次数)
    print(im)
    j +=1
    return newton_pol(im1,im,im3,j)
def t_pol(t,x,L):
    T = []
    for i in range(0,t):
        T.append(taloy_pol(x+i*1e-4,L))
    return T
def newton_pol_cr(im1,im2):
    im1.append(None)
    L = []
    T = []
    for i in range(1,len(im1)):
        if im1[i]!=im1[i-1] and im1[i]!=im1[i+1]:
            L.append(im2[i])        
        elif im1[i] == im1[i-1] and im1[i]==im1[i+1]:
            T.append(im2[i-1])
        else:
            T.append(im2[i-1])
            T.append(im2[i])
            L.extend(t_pol(len(T),))

a = t_pol(2,0,[0,1,5])
b = [0]
c = t_pol(3,1.5,[1.5,2,-1,2])
L=newton_pol([0,0+1e-4,1,1.5,1.5+1e-4,1.5+2e-4],a+b+c)
print(L)