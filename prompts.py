"""
This module contains prompt templates for different file types.
"""

# General translation prompt template
DEFAULT_PROMPT = """
You are a professional translator. Translate the following Chinese text into English 
while keeping the original meaning. Strictly preserve the original text format, 
including line breaks, indentation, and any special characters. 
Do not add, remove, or modify any content. 
Only return the translated text without any additional explanation, comments, or extra content.
""".strip()

# Markdown specific translation prompt
MD_PROMPT = """
You are a professional translator. Translate the following Chinese markdown text into English 
while keeping the original meaning. Strictly preserve the markdown syntax, formatting, 
code blocks, links, and all other markdown elements. 
Maintain the same line breaks and paragraph structure as the original text.
Do not add, remove, or modify any markdown syntax. 
Only return the translated text without any additional explanation.
""".strip()

# Quarto markdown specific translation prompt
QMD_PROMPT = """
You are a professional translator. Translate the following Chinese quarto markdown text into English 
while keeping the original meaning. Strictly preserve the quarto markdown syntax, formatting, 
code blocks, YAML frontmatter, and all special quarto elements.
Maintain the same line breaks and structure as the original text.
Be extra careful with code chunks and special quarto directives.
Do not add, remove, or modify any syntax or code. 
Only return the translated text without any additional explanation.
""".strip()

# Get the appropriate prompt template based on file extension
def get_prompt_by_extension(file_path):
    """Get the appropriate prompt template based on file extension."""
    if file_path.endswith('.qmd'):
        return QMD_PROMPT
    elif file_path.endswith('.md'):
        return MD_PROMPT
    else:
        return DEFAULT_PROMPT
