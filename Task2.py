for i in range (11):
    if i == 5:
        for j in range(3):
            print (13*"# ")
    print("# # #               # # #")
print ("")
print ("")
for i in range(4):
    if i == 2:
        for j in range(6):
            print (10*" " + 3*"# ")
    print (13*"# ")
print ("")
print ("")
for i in range (11):
    print (2*("# "), i*(" "), 2*("# "), (10-i)* ("  "), 2*("# "), i*(" "), 2*("# "))
print (" ")
print (" ")
for i in range (9):
    if i == 6 or i == 7:
        print((10 - i) * " " + (i+4) *"# ")
    else:
        print ((10 - i) * " " +"# #" + i * "  " + "# #")