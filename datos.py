logo = """ ____  ____   __  ____   __    ___   __   _  _  ____ 
(  _ \(  _ \ /  \(  _ \ /  \  / __) / _\ ( \/ )(  __)
 ) __/ )   /(  O )) __/(  O )( (_ \/    \/ \/ \ ) _) 
(__)  (__\_) \__/(__)   \__/  \___/\_/\_/\_)(_/(____)"""
tablas_proposiciones = [
    {
        "nombre": "Conjunción\n(P ∧ Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Disyunción\n(P ∨ Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Condicional\n(P → Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Bicondicional\n(P ↔ Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Disyunción Exclusiva\n(P ⊕ Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Negación Conjunta\n(¬(P ∨ Q))",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | F |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Negación Alternativa\n(¬(P ∧ Q))",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Condicional Inverso\n(Q → P)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | V |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Negación de P\n(¬P)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | F |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Negación de Q\n(¬Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Afirmación de P\n(P)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | V |
| F | V | F |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Afirmación de Q\n(Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "No-implicación Directa\n(P ∧ ¬Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | F |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "No-implicación Inversa\n(¬P ∧ Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | F |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Tautología\n(V)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Contradicción\n(F)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | F |
| F | V | F |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Negación del Condicional\n(¬(P → Q))",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | F |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Condicional con P Negada\n(¬P → Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Condicional con Q Negada\n(P → ¬Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Bicondicional Negado\n(¬(P ↔ Q))",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |
+---+---+---+"""
    },
    {
        "nombre": "Implicación Compuesta\n((P → Q) ∧ (Q → P))",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Disyunción Negaciones\n(¬P ∨ ¬Q)",
        "tabla": """\n\n\n+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Implicación\n((P ∧ Q) → R)",
        "tabla": """\n\n\n+---+---+---+---+
| P | Q | R | ? |
+---+---+---+---+
| V | V | V | V |
| V | V | F | F |
| V | F | V | V |
| V | F | F | V |
| F | V | V | V |
| F | V | F | V |
| F | F | V | V |
| F | F | F | V |
+---+---+---+---+"""
    },
    {
        "nombre": "Disyunción Exclusiva\n(P ⊕ Q ⊕ R)",
        "tabla": """\n\n\n+---+---+---+---+
| P | Q | R | ? |
+---+---+---+---+
| V | V | V | V |
| V | V | F | F |
| V | F | V | F |
| V | F | F | V |
| F | V | V | F |
| F | V | F | V |
| F | F | V | V |
| F | F | F | F |
+---+---+---+---+"""
    },
    {
        "nombre": "Consenso\n((P∧Q)∨(Q∧R)∨(P∧R))",
        "tabla": """\n\n\n+---+---+---+---+
| P | Q | R | ? |
+---+---+---+---+
| V | V | V | V |
| V | V | F | V |
| V | F | V | V |
| V | F | F | F |
| F | V | V | V |
| F | V | F | F |
| F | F | V | F |
| F | F | F | F |
+---+---+---+---+"""
    }
]