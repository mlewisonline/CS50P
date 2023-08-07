import random

def main():
    score = 0
    level = get_level()
    questions = generate_questions(level)


    for question in questions:
       user_answer = 0
       fail_count = 0
       x, y = question
       correct_answer = x + y

       while True:
            try:
                #Ask user for answer to question
                user_answer = int(input(f"{x} + {y} = "))
            except ValueError:
                # If user enters non int number increase fail count and break
                # On 3 wrong answers
                print("EEE")
                fail_count += 1
                if fail_count == 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    continue
            else:
                # Logic to check users answer is correct or wrong
                if user_answer == correct_answer and fail_count < 3:
                    score += 1
                    break
                else:
                    print("EEE")
                    fail_count += 1
                    if fail_count == 3:
                        print(f"{x} + {y} = {x+y}")
                        break


    print(f"Score: {score}")


# Get Level from user making sure its between 1 and 3 inclusive
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0  and level < 4:
                return level

        except ValueError:
            pass

# Generate Random numbers based on Level
def generate_integer(level):
    try:
        if  level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError

# generate 10 questions based on Level
def generate_questions(level):
    questions = []
    for _ in range(10):
        questions.append((generate_integer(level),generate_integer(level)))
    return questions


if __name__ == "__main__":
    main()