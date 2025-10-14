def taloy_pol(x,L):#泰勒多项式,x为自变量,L为一列表，存放了[x0,f(x0),...]‘...’表示f的n阶导数
    sum = L[-1]
    for i in range(2,len(L)):
        if i ==len(L):
            sum*=(x-L(0))
            sum+=L[1]
        sum =sum*(x-L[0])/(len(L)-i)
        sum +=L[-i]
    return sum
def newton_pol(im1,im2,im3=None):
    im = []
    if im3 == None:
        im3 = []
    im3.append(im2[0])
    print(im3)
    if len(im1)==1:
        return im3
    for i in range(1,len(im2)):
        im.append((im2[i]-im2[i-1])/(im1[i]-im1[i-1]))
    return newton_pol(im1[1:],im,im3)
a=newton_pol([1,2,3,4],[2,4,6,8])
print(a)