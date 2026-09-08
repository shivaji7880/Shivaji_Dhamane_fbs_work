class Television:
    def main(self):
        try:
            model_no=int(input("Enter model no:"))
            count=0
            temp=model_no
            while temp!=0:
                temp//=10
                count+=1
            # print(count)
            if count>4:
                raise Exception('Model_no should be of less than 5 digits..')
            screen_size=int(input("Enter screen size:"))
            if screen_size<12:
                raise Exception("Screen size should not smaller than 12")
            price=float(input("enter price:"))
            if price<0 or price>5000:
                raise Exception("Price is out of range.....")
        except Exception as e:
            print(e)
        else:
            print(f"Model no:{model_no}\tScreen Size:{screen_size}inches\tPrice:{price}")
        if Exception:
            print(f"Model no:0000\tScreen Size:0000\tPrice:0000")
            
t=Television()
t.main()      