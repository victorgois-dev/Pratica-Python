palavra = input("digite uma plavra e vermemos se ela é palindrama")
inverse = palavra[::-1]
if palavra == inverse:
    print("palindrama")
else:
    print("normal")