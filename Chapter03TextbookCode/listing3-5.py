"""Style some text with HTML tags."""

text: str
styling: str

# Obtain the text to be styled.
text = input("Please enter the text: ")

# Obtain the desired styling.
styling = input("Do you want strong (S) or emphasized (E) text?: ")

# Style the text.
if styling == "S":
    text = "<strong>" + text + "</strong>"
elif styling == "E":
    text = "<em>" + text + "</em>"

# Display the new text string.
print("{}".format(text))
