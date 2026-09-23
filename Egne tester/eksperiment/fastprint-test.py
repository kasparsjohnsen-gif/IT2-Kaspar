import time

def fast_print(text, speed=0.1):
    for letter in text:
        # end='' prevents a new line, flush=True forces immediate printing
        print(letter, end='', flush=True)
        time.sleep(speed)
    print() # Prints a final newline at the end

fast_print("This sentence is being typed out rapidly!")