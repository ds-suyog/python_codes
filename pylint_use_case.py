""" 
expected outut: 
1
2
3

output:
3
3
3
"""

list_of_printers = []
for i in [1, 2, 3]:
    def printer():
        print(i)
    list_of_printers.append(printer)

for func in list_of_printers:
    func()

