import openai
import requests
import re
import json

# Queries ChatGPT to generate a website
def gen_html(prompt):
    openai.api_key = '<YOUR-OPENAI-API-KEY-HERE>'
    
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

# Queries Stable Diffusion to generate images.
def generate_ai_img(prompt):
    
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
    "key": "<YOUR-STABLE-DIFFUSION-API-KEY-HERE>",
    "prompt": prompt,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)["output"][0]
    return result


def add_ai_imgs(html):
    
    descriptions = re.findall(r'\[(.*?)\]', html)
    generated_images = []

    for desc in descriptions:
        img_link = generate_ai_img(desc)
        generated_images.append(img_link)

    for match in descriptions:
        html = html.replace(f"[{match}]", generated_images.pop(0), 1)

    return html

def gen_full_site(prompt, save_file):
    try:
    # Generate HTML
        html_code = gen_html(prompt)
        html_code = add_ai_imgs(html_code)

        # Save the generated HTML
        html_file = open(save_file, "w")
        html_file.write(html_code)
    except:
        print("Generation failed. Please try again.")