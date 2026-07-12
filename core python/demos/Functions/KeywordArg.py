# Keyword argument 

def emp(id,name,sal,dept):
    data=f'Id:{id}\nName:{name}\nSalary:{sal}\nDepartment:{dept}'
    return data

res=emp('132',sal=35000,name='Shivaaa',dept='IT')
print(res)