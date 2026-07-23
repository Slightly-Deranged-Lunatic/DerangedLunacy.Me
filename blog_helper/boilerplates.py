def get_blog_post_boilerplate(dates):
    month_name = dates["month_name"]
    month = dates["month"]
    day = dates["day"]
    day_name = dates["day_name"]
    year = dates["year"]
    boilerplate = f"""<!DOCTYPE html>

<head>
    <title>
        {month} {day} {year}
    </title>
    <style>
        @import url("../../../../css/style.css");
    </style>
</head>

<html>
    <body>
        <h1>
            {day_name}, {month_name} {int(day)}{get_ordinal(day)}, {year}
        </h1>
        <p>
            text here meowmeowmewmewmoweo
        </p>
        <footer>
            <a href = "blogs.html"> Go back to the {month_name} blogs </a> <br>
            <a href = "../list.html"> Go back to the {year} blogs </a> <br>
            <a href = "../../blog_homepage.html"> Go back to all blogs </a> <br>
            <a href = "../../../../index.html"> Go back to the homepage </a>
        </footer>
    </body>
</html>"""

    return boilerplate

def get_blogs_list_boilerplates(dates):
    month_name = dates["month_name"]
    year = dates["year"]
    boilerplate = f"""<!DOCTYPE html>

<head>
    <title>
        {month_name} {year} Blogs
    </title>
    <style>
        @import url("../../../../css/style.css");
    </style>
</head>

<html>
    <body>
        <h1>
            {month_name} {year} Blogs
        </h1>
        <li>

        </li>
        <footer>
            <a href = "../list.html"> Go back to the {year} blogs </a> <br>
            <a href = "../../blog_homepage.html"> Go back to all blogs </a> <br>
            <a href = "../../../../index.html"> Go back to the homepage </a> <br>
        </footer>
    </body>
</html>"""
    return boilerplate

def get_ordinal(number):
    # Automatically assign a numbers ordinal based off of the last digit
    SPECIAL_CASES = ["11", "12", "13"] # These numbers always use "th" despite ending in 1, 2, and 3, hence they're special cases
    last_number = number[-1]
    if number in SPECIAL_CASES:
        return "th"
    elif last_number[-1] == "1":
        return "st"
    elif last_number[-1] == "2":
        return "nd"
    elif last_number[-1] == "3":
        return "rd"
    else:
        return "th"