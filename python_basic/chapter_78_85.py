filename = '01012020_sales.xlsx'

if ".xlsx" in filename:
    print("yes")


code = 'DSVNDOICSN'

if code == code.upper():
    print("all lethers is uppercase!!! ")

else :
    print("lowercase or number contain is given sttring")


number = 1.0
if isinstance(number,int):
    print("yes ")

else : print("no")



password = 'cskdnasdasda#!'
if len(password)>=11:  print("password correct")
else : print("password to short")



password = 'cskdnjasdsad!'
if (len(password)>=11) and ("!") in password : print("password correct")
else: print("password is incorrect")




project_ids = ['02134', '24253']
project_id = '02135'


if project_id in project_ids:
    print("correct")
else :
    project_ids.append(project_id)
    print(project_ids)



project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}


if (project_ids.get("02")=="new"):
    project_ids["02"] = "open"
    print(project_ids)



item = '001'
items = ['001', '000', '003', '005', '006']


if item in items:
    items.remove(item)
    print(items)





