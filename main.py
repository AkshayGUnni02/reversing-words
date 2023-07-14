def reverse_words(input_string):
    words = input_string.split()
    if len(words) != 2:
        return "Please provide exactly two words separated by a space."
    else:
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
input_str = input("Enter two words: ")
reversed_str = reverse_words(input_str)
print("Reversed words:", reversed_str)
print("End")
