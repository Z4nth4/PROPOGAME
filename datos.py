logo = """ ____  ____   __  ____   __    ___   __   _  _  ____ 
(  _ \(  _ \ /  \(  _ \ /  \  / __) / _\ ( \/ )(  __)
 ) __/ )   /(  O )) __/(  O )( (_ \/    \/ \/ \ ) _) 
(__)  (__\_) \__/(__)   \__/  \___/\_/\_/\_)(_/(____)"""
tablas_proposiciones = [
    {
        "nombre": "Conjunción\n(P ∧ Q)",
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | F |
| F | V | F |
| F | F | V |
+---+---+---+"""
    },
    {
        "nombre": "Negación Alternativa \n(¬(P ∧ Q))",
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
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
        "tabla": """+---+---+---+
| P | Q | ? |
+---+---+---+
| V | V | F |
| V | F | V |
| F | V | F |
| F | F | V |
+---+---+---+"""
    }
]