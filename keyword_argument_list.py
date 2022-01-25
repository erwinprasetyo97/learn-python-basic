def create_html(tag, text, **attribut):
    html = f"<{tag}"

    for key,value in attribut.items():
        html = html + f" {key} = '{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "hello world")
print(html)
html = create_html("a ", "ini adalah link", href="www.google.com", style="link")
print(html)