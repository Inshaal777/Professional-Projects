def get_favorite_animal():
    try:
        favorite_animal = input("What's your favorite animal? ").strip()

        if not favorite_animal:
            raise ValueError("My favorite animal is Cow! ")
        print(f"My favorite animal is also {favorite_animal}!")

    except ValueError as e:
        print(e)
        get_favorite_animal()

if __name__ == "__main__":
    get_favorite_animal()