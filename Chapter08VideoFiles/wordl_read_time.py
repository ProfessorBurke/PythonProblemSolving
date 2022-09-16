import os.path
import typing
import time

def read_words(file_name: str) -> list:
    """Open file_name and read the words in it to a list.
       Words are organized in the file one to a line.
       Return the list, or the empty list if there is an
       error with the file.
    """
    file: typing.TextIO
    words: list = []
    if os.path.isfile(file_name):
        file = open(file_name)
        words = file.readlines()
        file.close()
    return words
    
words = read_words("words")
old_time: int = time.perf_counter_ns()
"ddddd" in words
new_time: int = time.perf_counter_ns()
print(new_time - old_time)

s: set = set(words)
old_time = time.perf_counter_ns()
"ddddd" in s
new_time = time.perf_counter_ns()
print(new_time - old_time)



