name = "tamar"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
#"nika"  არის ცვლადითვის მნიშვნელობა

surname = "khvedelidze"

print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "nika" #ეს არის str (string) ტიპის ცვლადი
age =12 # ეს არის int integer მთელი რიცხვი
height = 184.5 #ეს არის  float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True  #True ან False
is_ugly = False #snakecase (უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False#. ჯავასკრიპტული.camelcase


print(name + " " + surname)  

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
#print(name + age)

#orint(type(age))
#orint(type(name))
#orint(type(surname))
#orint(type(height))
#orint(type(knows_programming))

print(name + " " + str(age))


name = input()

print("hello", name)