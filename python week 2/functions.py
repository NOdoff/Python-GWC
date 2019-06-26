
# --- Define your functions below! ---
def is_even(num):
    return(num%2 == 0)
def calc_total(list):
    sum = 0
    for num in list:
        sum+=num
    return sum
def how_many_a(some_string):
    count = 0
    for character in some_string:
        if(character == 'a'):
            count+=1
    return count
def how_many_specific_characters(character, some_string):
    count = 0
    for char in some_string:
        if(character == char):
            count+=1
    return count
# --- Put your main program below! ---
def main():
    # print(is_even(9))
    # print(calc_total([1,2,3,4,5]))
    print(how_many_specific_characters('t','tttt'))




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
