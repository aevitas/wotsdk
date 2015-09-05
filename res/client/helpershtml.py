# Embedded file name: scripts/client/helpers/html.py


def htmlEscape(text):
    """Produce entities within text."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')