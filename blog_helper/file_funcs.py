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
    blog_name = f"{dates["full_date"]}.html"
    if blog_name not in os.listdir():
        with open(blog_name, "w") as file:
            print(f"Made {blog_name} in {os.getcwd()}")
            file.write(boilerplates.get_blog_post_boilerplate(dates))

def get_li_element_line(file, html_id):
    # Gets the line number of the opening <li> for the respective file content with the ID, assuming the directories are correct
    with open(file) as file_contents:
        data = file_contents.readlines()
    stripped_data = []
    for line in data:
        stripped_data.append(line.strip())
    line = stripped_data.index(f'<li id = "{html_id}">') + 1 # Python lists start at 0 and we can't have line 0 in a file
    return line

def insert_content(file_name, content, line):
    # Will automatically append a \n
    with open(file_name) as file:
        file_content = file.readlines()

    # Add indentation
    comparison_string = file_content[line]
    leading_spaces = len(comparison_string) - len(comparison_string.lstrip())
    for i in range(leading_spaces):
        content = " " + content
    file_content.insert(line - 1, content + "\n") # I don't know why this - 1 has to be here for the expected result but its here now so!
    print(file_content)
    with open(file_name, "w") as file:
        file.writelines(file_content)

def read_file_line(file_name, line):
    with open(file_name) as file:
        content = file_without_whitespace(file)
    return content[line - 1]

def should_edit_file(file, html_id, expected_line):
    first_list_item_line = get_li_element_line(file, html_id) + 1
    first_list_item = read_file_line(file, first_list_item_line)
    if first_list_item == expected_line:
        print(f"No need to edit the content of {file}")
        return False
    else:
        print("File contents need to be edited")
        print(f"Content of file: {first_list_item}, expected: {expected_line}")
        return True

def add_indentation(file_name, line, string_to_indent):
    # Determines how many spaces should be added to a string based off of a files lines
    with open(file_name) as file:
        content = file.readlines()
    comparison_string = content[line - 1]
    leading_spaces = len(comparison_string) - len(comparison_string.lstrip())
    for i in range(leading_spaces):
        string_to_indent = " " + string_to_indent

def edit_files(dates):
    year = dates["year"]
    month_name = dates["month_name"]
    full_date = dates["full_date"]
    day_name = dates["day_name"]

    # Edit all of the HTML files if applicable

    # blog_homepage.html
    file = "blog_homepage.html"
    expected_line = f'<a href = "{year}/list.html"> {year} Blogs </a>'
    html_id = "year_list"
    first_list_item_line = get_li_element_line(file, html_id) + 1

    if should_edit_file(file, html_id, expected_line):
        insert_content(file, expected_line, first_list_item_line)
    os.chdir(year)

    # list.html
    file = "list.html"
    expected_line = f'<a href = "{month_name}/blogs.html"> {month_name} {year} </a>'
    html_id = "month_list"
    first_list_item_line = get_li_element_line(file, "month_list") + 1

    if should_edit_file(file, html_id, expected_line):
        insert_content(file, expected_line, first_list_item_line)
    os.chdir(month_name)

    # blogs.html
    file = "blogs.html"
    expected_line = f'<a href = "{full_date}.html"> {full_date.replace("_", "-")} {day_name} </a> <br>'
    html_id = "blog_list"
    first_list_item_line = get_li_element_line(file, "blog_list") + 1

    if should_edit_file(file, html_id, expected_line):
        insert_content(file, expected_line, first_list_item_line)

def file_without_whitespace(file):
    # I don't like dealing with tabs nor any \n in the list from file.readlines() so this is here
    file_without_whitespace = []
    for item in file:
        file_without_whitespace.append(item.strip())
    return file_without_whitespace
