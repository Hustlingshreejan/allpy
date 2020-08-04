print("This is a dictionary")
d={"Egg":"Anda","Rice":"Bhaat","Meat":"masu"}
user=input("What you want to search: ")
print("meaning for the word",user,":",d.get(user,"not found"))
