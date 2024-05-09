# input : ["apel","jeruk","mangga","pisang"."anngur","durian"]
# output :  ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

buah = ["apel","jeruk","mangga","pisang","anngur","durian"]
keluaran = []

for i in buah:
    if len(i) >= 5:
        keluaran.append(i)
keluaran.sort()
print(keluaran)

