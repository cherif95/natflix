import datetime
import csv
import utils

existing_users = []
with open("users.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        existing_users.append(
            {
                "name": row[0],
                "email": row[1],
                "age": row[2],
                "country": row[3],
                "subscription_type": row[4],
                "password": row[5],
            }
        )



existing_email_address = set([user["email"] for user in existing_users])


def register():
    name = None
    while name is None:
        name = input("Veillez entrer votre nom: ")
        if name.strip() == "":
            name = None

    email = None
    while email is None:
        email = input("Veillez entrer votre email: ").lower()
        if not utils.is_a_valid_email_address(email):
            print("L'adresse email invalide!")
            email = None

        if email in existing_email_address:
            print("Adresse email deja utilisée!")
            email = None

    birth_year = None
    while birth_year is None:
        birth_year = input("Entrer votre année de naissance: ")
        if not birth_year.isdigit():
            print("L'année de naissance doit être positif!")
            birth_year = None
    age = datetime.datetime.now().year - int(birth_year)

    country = None
    while country is None:
        country = input("Veillez entrer votre pays: ")

        if country.strip() == "":
            print("Le pays entré est invalide")
            country = None

    subscription_type = None
    while subscription_type is None:
        subscription_type = input(
            "Veillez entrer votre type d'abonnement 1 - [Régional] 2 - [International]: "
        )

        if subscription_type not in ("1", "2"):
            print(
                "Le type d'abonnement doit être 1 pour regional et 2 pour international."
            )
            subscription_type = None

    password = None
    while password is None:
        password = input("Veillez entrer votre mot de passe: ")

        if len(password) < 6 or password.isspace():
            print("Mot de passe min 6 caractères et ne doit pas contenir d'espaces")
            password = None

    print(f"{name=} {email=} {age=} {country=} {subscription_type=} {password=}")

    user = {
        "name": name,
        "email": email,
        "age": age,
        "country": country,
        "subscription_type": int(subscription_type),
        "password": password,
    }

    with open("users.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, age, country, subscription_type, password])

    return user


def authenticate():
    email = None
    while email is None:
        email = input("Veillez entrer votre email: ").lower()
        if not utils.is_a_valid_email_address(email):
            print("L'adresse email invalide!")
            email = None
            continue

        if email not in existing_email_address:
            print("Aucun utilisateur ne correspond à cette adresse email!")
            email = None

    user_found = None
    for u in existing_users:
        if u["email"] == email:
            user_found = u

    password = None
    while password is None:
        password = input("Veillez entrer votre mot de passe: ")

        if user_found["password"] != password:
            print("Mot de passe invalide")
            password = None

    return user_found
