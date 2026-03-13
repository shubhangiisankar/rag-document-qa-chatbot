import re


def format_answer(text):

    sections = []
    seen_titles = set()

    pattern = r'(Annual Leave|Sick Leave|Maternity Leave|Emergency Leave):\s*([^\.]+)'

    matches = re.findall(pattern, text)

    for title, description in matches:

        title = title.strip()
        description = description.strip()

        # remove duplicates
        if title not in seen_titles:
            sections.append({
                "title": title,
                "description": description
            })
            seen_titles.add(title)

    return sections