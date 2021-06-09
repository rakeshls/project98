def SwapFileData():
     swap1 = input("Enter 1st file name to Swap:-  ")
     swap2 = input("Enter 2nd file name to Swap:-  ")
     
     with open(swap1, 'r') as a:
         read_a = a.read()
     
     with open(swap2, 'r') as b:
         read_b = b.read()

     with open(swap1, 'w') as a:
         a.write(read_b)

     with open(swap2, 'w') as b:
         b.write(read_a)


print()
print('Swapping File Data - Project')
print('This project by Niyati Singh')
print()
SwapFileData()
print()
print("Data Swapped Successfully")
print()
print("Thank you for using Swapping File Data")
print("Run the terminal again to reswap the data in the files.")