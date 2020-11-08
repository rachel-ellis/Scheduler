import sys 
def safe_input(f=None, prompt=""):

    # Case:  Stdin
    if f is sys.stdin or f is None:
        line = input(prompt)
    # Case:  From file
    else:
        break
    return(line.strip(), True)
