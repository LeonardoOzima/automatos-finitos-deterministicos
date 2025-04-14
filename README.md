# Autômatos Finitos Determinísticos em Python

Este projeto contém implementações em Python de diversos **Autômatos Finitos Determinísticos (AFDs)**, desenvolvidas como parte dos estudos em **Teoria da Computação**.

## 🧠 Objetivo

Simular diferentes AFDs que reconhecem linguagens formais específicas, utilizando uma única função base que recebe uma definição de máquina e uma cadeia de entrada.

## ⚙️ Implementação

A função principal usada em todos os exercícios é a seguinte:

```python
def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F
```

## 📂 Exercícios Implementados

Cada AFD é definido com sua respectiva tupla `(Q, Sigma, delta, q0, F)` e testado com cadeias de exemplo.

### ✅ Exercícios disponíveis:

- **M4**: Linguagem L4 = { baⁿba | n ≥ 0 }
- **M5**: Linguagem L5 = { x ∈ {a, b}* | |x| mod 3 = 0 }
- **M6**: Linguagem L6 = { w ∈ {a, b}* | (|w|ₐ + |w|ᵦ) mod 2 = 0 }
- **M7**: Linguagem L7 = { a^m b^n | m,n ≥ 0 ∧ (m+n) mod 2 = 0 }
- **M8**: Linguagem L8 = { x ∈ Σ* | x termina com dígito par }
- **M9**: Linguagem L9 = { x ∈ Σ* | x termina com 0 ou 5 (múltiplo de 5) }
- **Mex**: Linguagem L = { w ∈ {a,b}* | quantidade de a’s é ímpar ∧ quantidade de b’s é múltipla de 3 }

## ▶️ Execução

Você pode executar o script diretamente com Python 3:

```bash
python3 afd_exercicios.py
```

Cada AFD será executado com exemplos de cadeias e indicará se foi **aceita** ou **rejeitada**.

## 📘 Requisitos

- Python 3.x
