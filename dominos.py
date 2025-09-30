#Dominos Clone

import random
class Dominos:
    #Data
    menu={
        "veg":{"margerita":129,"cheese_and_corn":169,"peepi_paneer":260,"veg_loaded":210,"tomato_tangi":170},
        "Non_veg":{"pepper_barbeque":199,"non_veg_loaded":169,"chicken_sausage":200},
        "Snacks":{"garlic_bread":120,"zingy":59,"chicken_cheese_balls":170},
        "Desserts":{"choco_lava":100,"mousse cake":169},
        "Drings":{"coke":90,"pepsi":78,"sprite":50}
    }
    
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False#to validate login status
        self.cart={}#to store orders
        
        #MAIN PROGRAM
        while True:
            if not self.login_status:
                print("--------WELCOME TO DOMINOS 🍕🍕🍕 APP---------")
                print("Login")
                ch=input("Do you want to Login ? (y/n):").lower()
                if ch=='y':
                    self.login()
        
            if self.login_status:
                print("--------------------------------------------------------------")
                print("User 👤👤:",self.name)
                print("Enter 1:Order")
                print("Enter 2:Show cart")
                print("Enter 3:Logout") 
                choice=int(input("Enter choice:"))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice")
                        
                
              
    @staticmethod
    def validate_otp(value):
        while True:
            print("'-----------------------------------------------------")
            og_otp=random.randint(1000,9999)
            print(f"An OTP has been sent to{value}") 
            print(f"Your dominos OTP is:{og_otp}")
            otp=int(input("Enter OTP:")) 
            if otp == og_otp:
                print("Login Successful✅✅")
                return True
            print("Incorrect OTP Enter correct OTP.....")   
            
        
        
               
            
    
    def login(self):
        print("Enter 1:Login with phno ")
        print("Enter 2:Login with email")
        ch=int(input("Enter your choice:"))
        if ch==1:
            #phone number validation
            phno=int(input("Enter phno:"))
            if phno == self.phno:
                state=self.validate_otp(phno)#True
                self.login_status=state
            else:
                print("Incorrect OTP")      
        elif ch==2:
           #email validation
           email=input("Enter your email:")
           if email == self.email:
              state=self.validate_otp(email)
              self.login_status=state
           else:
               print("Incorrect Email")
               
        else:
           print("Invalid email")
    
    
    def order(self):
        print("-----------Dominos Menu--------------")
        for category in Dominos.menu:
            print(category)
        cat=input("Enter category:")
        if cat in Dominos.menu:
            
            d=Dominos.menu[cat]
            for item in d:#display item for respective category
                print(item,'        Rs.',d[item])
            item=input("Enter Item:")
            if item in d:
                q=int(input("Enter Quantity:"))
                if item in self.cart:
                                   
                    self.cart[item]+=d[item]*q #var[key]=new val
                else:
                    self.cart[item]=d[item]*q    
                print(f"{item} added to the cart🛒🛒")
                print(self.cart)
            else:
                print(f"{cat} is Not Available❌❌❌")         
        else:
            print(f"{cat} is Not Available❌❌❌")        
            
            
            
            
    def show_cart(self):
        print("-------------------------------------------------")
        if self.cart!={}:
            total_bill=0
            
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,'-----------Rs.',self.cart[item])
            print("Total Bill:          Rs.",total_bill)
        else:
            print("cart is Empty please order.....") 
            
        if self.cart!={}:
            ch=input("Do you want to place order ? (y/n)").lower()  
            if ch=="y":
                print("Thank you for placing the order..........")
                print("your order is on the way")
                self.cart={}                 
        
    def logout(self):
        ch=input("Do you want to logout?(y/n)").lower()
        if ch=='y':
            self.login_status=False
            print("Logged out✅")       
    
ob=Dominos("Dharshini","darshini.2007@gmail.com",9894252550)

  