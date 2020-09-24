import webbrowser, argparse

while True:
    query = input("Enter Google Search query:\n").split(" ")
    query = " ".join(f'%22{q}%22' for q in query) + "+after%3A2019+-quora+-pinterest"
    webbrowser.open("https://www.google.com/search?q=" + query)

    # webbrowser.open("https://www.google.com/search?tbm=isch&q=" + query)

