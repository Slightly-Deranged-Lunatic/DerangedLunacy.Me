import os
from pathlib import Path
import html
import boilerplates
from datetime import date

def main():
    standardize_working_directory()
    date_object = date.today()
    dates = {
        "day" : date_object.strftime("%d"),
        "day_name" : date_object.strftime("%A"),
        "month" : date_object.strftime("%m"),
        "month_name" : date_object.strftime("%B"),
        "year" : date_object.strftime("%Y"),
        "full_date" : date_object.strftime("%d_%m_%Y")
    }

    make_html_file(dates)
    blog_post_boilerplate = boilerplates.get_blog_post_boilerplate(dates)
    list_boilerplate = boilerplates.get_blogs_list_boilerplate(dates)
    months_boilerplate = boilerplates.get_month_list_boilerplate(dates)

    write_boilerplate_to_post(dates, blog_post_boilerplate)

def standardize_working_directory():
    # Makes the working directory /html/subpages/my_blog no matter where the script is being ran from.
    # This way we can use relative paths.
    website_directory = os.path.dirname(__file__)
    os.chdir(website_directory)
    os.chdir(f"{Path.cwd().parent}/html/subpages/my_blog")
    print(os.getcwd())

def make_html_file(dates):
    # Undocumented year so we need to make a new year directory
    year = dates["year"]
    if year not in os.listdir():
        os.mkdir(year)
        print(f"Made the {year} directory in {os.getcwd()}")
    os.chdir(year)

    # Undocumented month so we need to make a new month directory
    month_directory = f"{dates["month_name"]}"
    if  month_directory not in os.listdir():
        os.mkdir(month_directory)
        print(f"Made the {month_directory} directory in {os.getcwd()}")
    os.chdir(month_directory)

    # Undocumented day so we need to make a new day html file
    html_file_name = f"{dates["full_date"]}.html"
    if html_file_name not in os.listdir():
        with open(html_file_name, "x") as file:
            print(f"Made the HTML file {html_file_name} in {os.getcwd()}")
    else:
        print(f"Could not make HTML file, does {html_file_name} exist in {month_directory}?")
    standardize_working_directory()

def write_boilerplate_to_post(dates, blog_post_boilerplate):
    os.chdir(f"{dates["year"]}/{dates["month_name"]}")
    print(f"Changed directory to {os.getcwd()}")
    with open(f"{dates["full_date"]}.html", "w") as blog_post:
        blog_post.write(blog_post_boilerplate)
    print("Blog boilerplate written to blog file")
    standardize_working_directory()

if __name__ == "__main__":
    main()

#TODO: Edit the respective files to point to the new HTML file that was made