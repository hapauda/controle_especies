import random

num =int(input("coloque o numero da população: "))
# numero da população de especies
abelhas_pequenas = num

for abelhas in range(abelhas_pequenas):
    # abelhas de 1 a 4 podem morrer
    chance_de_morte = random.randint(0,4)
    if chance_de_morte == 4:
        abelhas_pequenas -= 1

abelhas_grandes = 0

for abelhas in range(abelhas_pequenas):
    num_babies = random.randint(0,3)
    abelhas_grandes += +num_babies

abelhas_pequenas = abelhas_grandes

print(str(abelhas_pequenas) + "  abelhas pequenas que sobreviveram")