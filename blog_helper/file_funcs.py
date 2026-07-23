import os
import boilerplates

def make_paths(dates):
    # Only makes the relevant paths we need if any, does not create any files itself.
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

def create_files(dates):
    # Creates the relevant files in paths and populates it with boilerplate html

    # Create list.html for the years
    year = dates["year"]
    os.chdir(year)
    if "list.html" not in os.listdir():
        with open("list.html", "w") as file:
            print(f"Made file list.html in {os.getcwd()}")
            file.write(boilerplates.get_month_list_boilerplate(dates))

    # Create blogs.html for the months
    month_name = f"{dates["month_name"]}"
    os.chdir(month_name)
    if "blogs.html" not in os.listdir():
        with open("blogs.html", "w") as file:
            print(f"Made blogs.html in {os.getcwd()}")
            file.write(boilerplates.get_blogs_list_boilerplate(dates))

    # Create new blog post
    blog_name = f"{dates["full_date"]}"
    if blog_name not in os.listdir():
        with open(blog_name, "w") as file:
            print(f"Made {blog_name} in {os.getcwd()}")
            file.write(boilerplates.get_blog_post_boilerplate(dates))