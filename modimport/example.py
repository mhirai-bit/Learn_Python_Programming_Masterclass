import webbrowser

# webbrowser.open("https://www.python.com", new=1)
chrome = webbrowser.get("google-chrome %s").open_new_tab("https://www.python.com")
