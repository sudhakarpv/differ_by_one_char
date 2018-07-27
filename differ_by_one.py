# differ_by_one_char
def main():
    pass
    n=input().split()
    k=n[0]
    j=n[1]
    flag=0
    list_1=list(k)
    list_2=list(j)
    print(list_1)
    print(list_2)
    for word in list_1:
        for word1 in list_2:
            if(word==word1):
               flag=0
            else:
                flag+=1
    if (flag==1):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
