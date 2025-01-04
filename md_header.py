from gpt_interaction import create_title

HEADER_MODEL = "title:<title>"

def write_github_page_header(page_body):
    generated_title = create_title(page_body)

    return HEADER_MODEL.replace("<title>", generated_title)
