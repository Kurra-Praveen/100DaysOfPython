from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "Squirrel", "Armando"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Praveen", "Praveen2"])
table.align = 'c'
print(table)
