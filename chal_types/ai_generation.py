import openai
import random

# Queries ChatGPT to generate a website
def gen_html(prompt):
    openai.api_key = '<YOUR-API-KEY-HERE>'
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None,
        n=1
    )

    return response.choices[0].text.strip()

# Adds all links in a file to a useable array
def format_links(file):
    formatted_links = []
    x = open(file, "r")

    links = x.readlines()
    for l in links:
        formatted_links.append(l)

    return formatted_links

def add_imgs(html, links):
    # Note that this is currently the most optimal way to implement image generation. Attempts to generate via jinja templates confuse ChatGPT, (because there are multiple requests being made at once, ex. json input, jinja template, etc.) generating suboptimal results.
    while "[PLACEHOLDER]" in html:
            currlink = random.choice(links)
            html = html.replace("[PLACEHOLDER]", currlink, 1)
    return html

def gen_full_site(prompt, links, save_file):
    # Generate HTML
    html_code = gen_html(prompt)
    links = format_links(links)
    html_code = add_imgs(html_code, links)

    # Save the generated HTML
    html_file = open(save_file, "w")
    html_file.write(html_code)
