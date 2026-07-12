def emp(id='Not assigned',name='Unknown',sal='10000',dep='Reception', email='abc@123',address='pune'):
    
    data=f'Id:{id}\nName:{name}\nSalary:{sal}\nDepartment:{dep}\nEmail:{email}\nAddress:{address}'
        
    return data

res=emp(id=101,name='Shivaji',sal='50000',dep='IT') 
print(res)