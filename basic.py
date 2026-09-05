data1=13
print(data1," : ", type(data1))
data2=13.5
print(data2," : ", type(data2))
data3="Hello"
print(data3," : ", type(data3))
data4=True
print(data4," : ", type(data4))
data5=13+2j
print(data5," : ", type(data5))
data6=[1,2,3,4,5]
print(data6," : ", type(data6))

statement="HelloWorld"
print(statement)
print(statement[0])
print(statement[0:3])
print(statement[2:7])
print(statement*2)
print(statement+" ByeWorld")

# list: store dupliacte and are chaneable e.g: list=[1,2,3,4,5,"hello",3,5]:
# duple: store duplicate and are unchangeable e.g: duple=(1,2,3,4,5,"hello",3,5): if you try to change them it will give error
# set: store unique values(No duplicate) and are changeable e.g: set={1,2,3,4,5,"hello"}: if you add dupliacte here it will automatically remove it
# range: like (1,10) it will give you 1,2,3,4,5,6,7,8,9

list_data = [11,12,13,14,15, 'orange']
tuple_data = (12,15,17 , 'kiran')
set_data = {'ali', 'hassan', 'ayesha' , 12 ,18.6}
range_data = range(1,11)
print('List Data : ', list_data)
print('Tuple Data : ',tuple_data)
print('Set Data : ',set_data)
for i in range_data:
    print(i , end=' ') 

# Non parametric Function:
def fun():
    print("\nThis is a non parametric function")
fun()

# parametric Function:
def fun1(name, age):
    print("Your name is "+name+" and your age is ",age)

fun1("Alyan",19)