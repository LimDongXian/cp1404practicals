import wikipedia


valid = False
while not valid:
    # Prompt the user for a page title or search phrase
    title = input("Enter page title: ")

    # Exit the loop if the user enters a blank input
    if not title:
        print("Thank you.")
        valid = True

    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary[:500] + "...")  # Print first 500 characters of the summary
        print(page.url)

    except wikipedia.PageError:
        print(f"Page id \"{title}\" does not match any pages. Try another id!")

    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
