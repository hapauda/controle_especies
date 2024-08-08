import random

num =str(input("coloque o numero da população: "))
# numero da população de especies
abelhas_pequenas = num

for abelhas in range(abelhas_pequenas):
    # abelhas de 1 a 4 podem morrer
    chance_de_morte = random.randint(0,4)
    if chance_de_morte == 4:
        abelhas_pequenas -= -1

print(str(abelhas_pequenas) + "abelhas pequenas que sobreviveram")