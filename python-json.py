print("This is Python Program")
A={
    "employee":{
        "name":"Lakshmi",
        "age" :"23",
        "salary":"20000",
        "gender":"Female",
        "marrital_status":False
    }
}
name=A["employee"]["name"]
age=A["employee"]["age"]
salary=A["employee"]["salary"]
gender=A["employee"]["gender"]
marrital_status=A["employee"]["marrital_status"]

if gender=="male":
    he_or_she="He"
else:
    he_or_she="She"

if marrital_status==True:
    marrital_status="Married"
else:
    marrital_status="Unmarried"

print(f"{name} is earning {salary} and {he_or_she} is {marrital_status}")
                                                                                                                                                                                                     
                                                                                                                                                              
