import openai
import random

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

def format_links(file):
    formatted_links = []
    x = open(file, "r")

    links = x.readlines()
    i = 0
    for l in links:
        if(l != "\n"):
            formatted_links.append(l.strip("\n"))
            i+=1
    return formatted_links

def add_imgs(html, links):
    while True:
        if "[PLACEHOLDER]" in html:
            currlink = random.choice(links)
            html = html.replace("[PLACEHOLDER]", currlink, 1)
        else:
            break
    return html

def gen_full_site(prompt, links, save_file):
    # Generate HTML
    html_code = gen_html(prompt)
    links = format_links(links)
    html_code = add_imgs(html_code, links)

    # Save the generated HTML
    html_file = open(save_file, "w")
    html_file.write(html_code)
