def main():
   camelCase = input("camelCase: ")
   snake_case = camel_case_to_snake_case(camelCase)

   print(f"snake_case: {snake_case}")


def camel_case_to_snake_case(input):
   result = ""
   for character in input:
      if character.islower():
         result = result + character
      else:
         result = result + ','
         result = result + character
   return result.replace(',', '_').lower()

if __name__ == "__main__":
    main()