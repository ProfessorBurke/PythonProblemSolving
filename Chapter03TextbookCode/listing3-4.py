"""Style some text with HTML tags."""

text: str
styling: str

# Obtain the text to be styled.
text = input("Please enter the text: ")

# Obtain the desired styling.
print("Please choose (S)trong, (E)mphasized, or (C)ode.")
styling = input("What is your choice? ")

# Style the text.
if styling == "S":
    text = "<p><strong>" + text + "</strong></p>"
elif styling == "E":
    text = "<p><em>" + text + "</em></p>"
elif styling == "C":
    text = "<p><code>" + text + "</code></p>"
else:
    text = "<p>" + text + "</p>"

# Display the new text string.
print("{}".format(text))
