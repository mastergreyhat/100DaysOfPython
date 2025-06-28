# import turtle

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


import prettytable

table = prettytable.PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Elecrtic"],
        ["Charmander", "Fire"],
        ["Squirtle", "Water"]
    ]
)
table.align = 'l'
print(table)