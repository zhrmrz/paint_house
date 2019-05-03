class Sol:
    def paint_house(self,n,k):
        p1=int((n+1)/2)
        return (k*((k-1)**(n-1)))+k**p1

if __name__ == '__main__':
    p1=Sol()
    print(p1.paint_house(2,4))
