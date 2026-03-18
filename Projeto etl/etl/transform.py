import re

def is_valid_email(email):
    if not email:
        return False
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_valid_phone(phone):
    if not phone:
        return False
    phone = re.sub(r"\D", "", str(phone))
    return 10 <= len(phone) <= 13

def is_valid_city(city):
    if not city:
        return False
    city = str(city).strip()
    # Apenas letras e espaços (com acento)
    return bool(re.match(r"^[A-Za-zÀ-ÿ\s]+$", city)) and len(city) >= 2

def clean_data(df):
    df = df.copy()
    descartados = {
        "email_invalido": 0,
        "nome_nulo": 0,
        "telefone_invalido": 0,
        "cidade_invalida": 0,
        "duplicados": 0
    }

    # Padronização
    df["nome"] = df["nome"].str.strip().str.title()
    df["cidade"] = df["cidade"].astype(str).str.strip().str.title()

    # Remover nulos
    before = len(df)
    df = df.dropna(subset=["nome", "email", "telefone", "cidade"])
    descartados["nome_nulo"] = before - len(df)

    # Email
    mask_email = df["email"].apply(is_valid_email)
    descartados["email_invalido"] = len(df) - mask_email.sum()
    df = df[mask_email]

    # Telefone
    mask_phone = df["telefone"].apply(is_valid_phone)
    descartados["telefone_invalido"] = len(df) - mask_phone.sum()

    print("Telefones inválidos:")
    print(df.loc[~mask_phone, "telefone"].tolist())

    df = df[mask_phone]

    # Cidade
    mask_city = df["cidade"].apply(is_valid_city)
    descartados["cidade_invalida"] = len(df) - mask_city.sum()

    print("Cidades inválidas:")
    print(df.loc[~mask_city, "cidade"].tolist())

    df = df[mask_city]

    # Duplicados
    before = len(df)
    df = df.drop_duplicates(subset=["email"])
    descartados["duplicados"] = before - len(df)

    print(f"\n{len(df)} registros válidos após limpeza")

    return df, descartados