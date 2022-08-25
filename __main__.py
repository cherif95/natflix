import sys
import users


def display_main_title():
    TITLE_WITH = 80

    print("#" * TITLE_WITH)
    print(f"|||{'Welcome to Natflix':^{TITLE_WITH - 6}}|||")
    print("-" * TITLE_WITH)


def display_home_menu_and_retrieve_user_choice():
    choice = None

    while choice is None:
        print("Menu d'accueil")
        print("1 - S'inscrire")
        print("2 - S'authentifier")
        print("3 - Quitter")
        choice = input("Veillez entrer votre choix: ")
        if choice not in ("1", "2", "3"):
            print(
                "Votre choix n'est pas dans la liste des options. Veuillez réessayez!"
            )
            choice = None
    return choice


def main():
    display_main_title()
    user_choice = display_home_menu_and_retrieve_user_choice()

    match user_choice:
        case "1":
            user_created = users.register()
            print(f"user created {user_created}")
        case "2":
            authenticated_user = users.authenticate()
            print(f"user authenticated {authenticated_user}")
        case "3":
            sys.exit()


if __name__ == "__main__":
    main()
