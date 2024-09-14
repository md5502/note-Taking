import language_tool_python as lt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from notes.models import Note


@login_required(login_url="/users/login")
def grammar_check(request, slug):
    # Fetch the note by slug
    note = get_object_or_404(Note, slug=slug)
    content = note.rendered_html  # Assuming the HTML content is what needs checking

    grammar_issues = []

    if content:
        # Initialize LanguageTool checker
        tool = lt.LanguageTool("en-US")  # Set to your desired language (e.g., "en-US")
        matches = tool.check(content)

        # Prepare grammar issues for display
        for match in matches:
            grammar_issues.append({  # noqa: PERF401
                "message": match.message,
                "offset": match.offset,
                "length": match.errorLength,
                "suggestions": match.replacements,
            })

    # Render a template to display the results
    return render(request, "grammar_check.html", {
        "note": note,
        "grammar_issues": grammar_issues,
    })
