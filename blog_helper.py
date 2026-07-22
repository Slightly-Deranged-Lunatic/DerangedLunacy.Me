import os
import html
from datetime import date
from sre_parse import SPECIAL_CHARS

def main():
    standardize_working_directory()
    date_object = date.today()
    dates = {
        "current_day" : date_object.strftime("%d"),
        "current_day_name" : date_object.strftime("%A"),
        "current_month" : date_object.strftime("%m"),
        "current_month_name" : date_object.strftime("%B"),
        "current_year" : date_object.strftime("%Y"),
        "current_date" : date_object.strftime("%d_%m_%Y")
    }

    os.chdir("html/subpages/my_blog")
    make_html_file(dates)
    standardize_working_directory()
    html_boilerplate = get_html_boilerplate(dates)

def standardize_working_directory():
    # Makes the working directory the website directory no matter where the script is being ran.
    # This way we can use relative paths.
    website_directory = os.path.dirname(__file__)
    os.chdir(website_directory)

def make_html_file(dates):
    # Undocumented year so we need to make a new year directory
    current_year = dates["current_year"]
    if current_year not in os.listdir():
        os.mkdir(dates["current_year"])
        print(f"Made the {current_year} directory in {os.getcwd()}")
    os.chdir(dates["current_year"])

    # Undocumented month so we need to make a new month directory
    month_directory = f"{dates["current_year"]}_{dates["current_month_name"]}"
    if  month_directory not in os.listdir():
        os.mkdir(month_directory)
        print(f"Made the {month_directory} directory in {os.getcwd()}")
    os.chdir(month_directory)

    # Undocumented day so we need to make a new day html file
    html_file_name = f"{dates["current_date"]}.html"
    if html_file_name not in os.listdir():
        with open(html_file_name, "x") as file:
            print(f"Made the HTML file {html_file_name} in {os.getcwd()}")
    else:
        print(f"Could not make HTML file, does {html_file_name} exist in {month_directory}?")

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

def get_html_boilerplate(dates):
    month_name = dates["current_month_name"]
    month = dates["current_month"]
    day = dates["current_day"]
    day_name = dates["current_day_name"]
    year = dates["current_year"]
    boilerplate = f"""
    <!DOCTYPE html>

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
                <a href = "../{year}_list.html"> Go back to the {year} blogs </a>
                <br>
                <a href = "../../blog_homepage.html"> Go back to all blogs </a>
                <br>
                <a href = "../../../../index.html"> Go back to the homepage </a>
            </footer>
        </body>
    </html>
    """
    return boilerplate

if __name__ == "__main__":
    main()

#TODO: Write the boilerplate HTML code to the new file
#TODO: Edit the respective files to point to the new HTML file that was made