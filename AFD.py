def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F

# Definição do AFD M4 para L4 = {𝑏𝑎^n * 𝑏𝑎 ∣ 𝑛 ≥ 0}

Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q3',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q4', 
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q3',
    ('q3', 'b'): 'q3',
    ('q4', 'a'): 'q3',
    ('q4', 'b'): 'q3',
}
q0 = 'q0'
F = {'q4'}

M4 = (Q, Sigma, delta, q0, F)

# Definição do AFD M5 para L5 = {𝑥 ∈ {𝑎, 𝑏}∗ ∣ |𝑥| mod 3 = 0}
Q = {'q0', 'q1', 'q2'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q0', 
    ('q2', 'b'): 'q0',
}

q0 = 'q0'
F = {'q0'}

M5 = (Q, Sigma, delta, q0, F)

# Definição do AFD M6 para L6 = 𝐿6 = {𝑤 ∈ {𝑎, 𝑏}∗∣ (|𝑤|𝑎 + |𝑤|𝑏) mod 2 = 0}
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q0', 
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q1',
    ('q3', 'b'): 'q2',
}
q0 = 'q0'
F = {'q0', 'q3'}

M6 = (Q, Sigma, delta, q0, F)

# Definição do AFD M7 para 𝐿7 =  {𝑎^𝑚𝑏^𝑛 ∣ 𝑚, 𝑛 ≥ 0 ∧ (𝑚 + 𝑛) mod 2 = 0}
Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3', 
    ('q2', 'b'): 'q4',
    ('q3', 'a'): 'q4',
    ('q3', 'b'): 'q2',
    ('q4', 'a'): 'q4',
    ('q4', 'b'): 'q4',
}
q0 = 'q0'
F = {'q0','q3'}

M7 = (Q, Sigma, delta, q0, F)

# Definição do AFD M8 para 𝐿8 =   {𝑥 ∈ Σ∗ ∣ 𝑥 mod 2 = 0}

Q = {'q0', 'q1', 'q2'}
Sigma = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
pares = {'0', '2', '4', '6', '8'}

delta = {
    #Vai ser preenchido pelo loop abaixo.
}

for estado in Q:
    for d in Sigma:
        if d in pares:
            delta[(estado, d)] = 'q1'
        else:
            delta[(estado, d)] = 'q2'
            
q0 = 'q0'
F = {'q1'}

M8 = (Q, Sigma, delta, q0, F)

# Definição do AFD M9 para 𝐿9 = {𝑥 ∈ Σ∗ ∣ 𝑥 mod 5 = 0}
Q = {'q0', 'q1', 'q2'}
Sigma = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
delta = {}

# Transições de q0
for d in Sigma:
    if d in {'0', '5'}:
        delta[('q0', d)] = 'q1'  # vai para o estado de aceitação
    else:
        delta[('q0', d)] = 'q2'  # vai para rejeição

# Transições de q1
for d in Sigma:
    if d in {'0', '5'}:
        delta[('q1', d)] = 'q1'  # permanece aceitando
    else:
        delta[('q1', d)] = 'q2'  # vai para rejeição
        
# Transições de q2
for d in Sigma:
    if d in {'0', '5'}:
        delta[('q2', d)] = 'q1'  # volta para aceitação
    else:
        delta[('q2', d)] = 'q2'  # permanece rejeitando
            
q0 = 'q0'
F = {'q1'}

M9 = (Q, Sigma, delta, q0, F)

# Obter um autômato finito que reconheça a linguagem L = {w ∈ {a, b} ∗ | w contém uma quantidade ímpar de símbolos a e uma quantidade múltipla de 3 de símbolos b}


Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3', 
    ('q2', 'b'): 'q4',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q5',
    ('q4', 'a'): 'q5',
    ('q4', 'b'): 'q0',
    ('q5', 'a'): 'q4',
    ('q5', 'b'): 'q1',
}
q0 = 'q0'
F = {'q1'}

Mex = (Q, Sigma, delta, q0, F)

# Testes
print("\n-=-=-=-=-=-=-=-=-=-\n")
print("M4")
print(AFD(M4, "baaaaba"))         # True (n=0)
print(AFD(M4, "baaaa"))      # True (n=1)

print("\n-=-=-=-=-=-=-=-=-=-\n")
print("M5")
print(AFD(M5, "abaaba"))         # True (n=0)
print(AFD(M5, "baaaa"))      # True (n=1)

print("\n-=-=-=-=-=-=-=-=-=-\n")
print("M6")
print(AFD(M6, ""))         # True (w=0)
print(AFD(M6, "a"))      # False (w=1)
print(AFD(M6, "ba"))      # True (w=2)

print("\n-=-=-=-=-=-=-=-=-=-\n")
print("M7")
print(AFD(M7, ""))         # True (w=0)
print(AFD(M7, "aabb"))      # False (w=4)
print(AFD(M7, "abab"))      # False "a" após "b"

print("\n-=-=-=-=-=-=-=-=-=-\n")
print("M8")
print(AFD(M8, ""))         # False (w=0)
print(AFD(M8, "23123234"))      # True, termina em par
print(AFD(M8, "312312341241"))      # False, termina em ímpar

print("\n-=-=-=-=-=-=-=-=-=-\n")

print("M9")
print(AFD(M9, ""))         # False (w=0)
print(AFD(M9, "232145"))      # True, termina em 5 ou 0
print(AFD(M9, "879827149872137982143"))      # False, não termina em 0 ou 5

print("\n-=-=-=-=-=-=-=-=-=-\n")
print("Ex")
print(AFD(Mex, "")) # False
print(AFD(Mex, "a")) # True
print(AFD(Mex, "aa")) # False
print(AFD(Mex, "abbb")) # True
print(AFD(Mex, "aaabbbbbb")) # True
