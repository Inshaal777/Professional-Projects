class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
def calculate_ages():
    anton = Friend("Anton", 21)
    beth = Friend("Beth", anton.age + 6)
    chen = Friend("Chen", beth.age + 20)
    drew = Friend("Drew", chen.age + anton.age)
    ethan = Friend("Ethan", chen.age)

    return [anton, beth, chen, drew, ethan]

def main():
    friends = calculate_ages()

    for friend in friends:
        print(friend)

if __name__ == "__main__":
    main()