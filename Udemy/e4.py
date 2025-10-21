import webbrowser

user_term = input("Enter the term you want to search:").replace(" ","+")

webbrowser.open(f"https://www.{user_term}.com")