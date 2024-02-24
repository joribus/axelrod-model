import random

k = [0, 1, 1, 1]
r = [0, 1, 0, 1]

k_r = []
posizioni = []
for i in range(len(k)):
    if k[i] != r[i]:
        posizioni.append(i)
        k_r.append(k[i])

n_kr = len(k) - len(k_r)
prob = n_kr / len(k)
print(prob)

# prendo un numero random tra 0 e 1 e interagiscono solo se prob sopra > di questo numero

sel = random.choice(posizioni)
k[sel] = r[sel]
print(k)
