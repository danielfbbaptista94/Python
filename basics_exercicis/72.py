import webbrowser


# settings_term = []

user_term = input('Enter with the keywords for Google search: ')
# settings_term.append(user_txt)

# for term in settings_term:
webbrowser.open_new_tab("https://google.com/search?q=%s" % user_term)
