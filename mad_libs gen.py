import random

fruits = ["Apple","Apricot","Banana","Berry","cherry","currant","Grape","Guava","Mango","Starfruit"]
random_fruit = random.choice(fruits)
vegetables = ["Artichoke","Celery","Chick Peas","Fennel","Lettuce","Onion","Peas","Squashes","Tomato"]
random_vegetable = random.choice(vegetables)
verb = str(input("enter a verb :"))
Color_Adjective = ["blue","gray","green","lemon","mango"]
random_color = random.choice(Color_Adjective)
Shape_Adjective = ["big","small","gigantic","mammoth","tall"]
random_shape = random.choice(Shape_Adjective)
Positive_Adj = input("enter a positive adjective:")
indefinite_pronoun = input("enter the indefinite pronoun: ")

def madlib_gen(a,b,c,d,e,f,g) :
    print("********Welcome to Madlib generator********")
    madlib_word=f"I love "+ Positive_Adj +" "+ random_fruit +" in "+ random_color + \
                " color and a "+ random_vegetable +" of "+ random_shape + " size for "+verb+" "+indefinite_pronoun +\
                " :) Thanks :)"

    print(madlib_word)

    with open('madlibfile.txt','a') as file_txt:
         file_txt.write(madlib_word + '\n')

madlib_gen(random_fruit,random_vegetable,verb,random_color,random_shape,Positive_Adj,indefinite_pronoun)

