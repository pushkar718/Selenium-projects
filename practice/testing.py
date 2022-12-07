import time

for i in range(1,10):
    restart=True
    while restart:
        restart=False
        for j in range(1,5):
            print("restart=true",i,j)
            time.sleep(0.2)
            if j == 3:
                break
        restart=True

        if restart==True:
            print("restart change")
            # if j==3:
            #     break
            # break

