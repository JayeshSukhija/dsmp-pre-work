# --------------
# Code starts here

class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)

# Code ends here


# --------------
# Code starts here

courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
a=courses['Math']
b=courses['English']
c=courses['History']
d=courses['French']
e=courses['Science']
total=a+b+c+d+e
print(total)

a=(total/5)
percentage=a
print(percentage)

# Code ends here


# --------------
# Code starts here

mathematics={'Geoffrey Hinton':78,'Andrew Ng':95, 'Sebastain Raschka':65,'Yoshua Benjio':50,
'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

topper = max(mathematics,key = mathematics.get)
print (topper)

# Code ends here 


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
a=topper.split()
print(a)
first_name=a[0]
print(first_name)
last_name=a[1]
print(last_name)

full_name=last_name+ " "+ first_name
print(full_name)

certificate_name=full_name.upper()
a=certificate_name
print(a)

# Code ends here


