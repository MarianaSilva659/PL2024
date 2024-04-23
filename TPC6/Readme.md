# TPC6: Gramática Independente de contexto


## Autor

- A100702
- Mariana Antunes Silva


## Resumo
    - Criar gramática independente de contexto LL(1)
    - Garantir prioridade dos operadores
    - Calcular todos os lookaheads 



```
    Start  p1 -> '?' var 
           p2 | '!' Body 
           p3 | var '=' Body

    Body   p4 -> '(' Body ')'
           p5 | Elem Expr

    Expr p6 -> Op Body
         p7 | ε

    Elem p8 -> num | var
    Op p9 -> '+' | '/' | '-' | '*'
```