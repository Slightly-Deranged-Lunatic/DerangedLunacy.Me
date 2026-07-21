import os
from datetime import date

def main():
    standardize_working_directory()
    date_object = date.today()
    dates = {
        "current_day" : date_object.strftime("%d"),
        "current_month" : date_object.strftime("%m"),
        "current_month_name" : date_object.strftime("%B"),
        "current_year" : date_object.strftime("%Y"),
        "current_date" : date_object.strftime("%d_%m_%Y")
    }

    os.chdir("html/subpages/my_blog")
    make_html_file(dates)
    standardize_working_directory()

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

if __name__ == "__main__":
    main()

#TODO: Write the boilerplate HTML code to the new file
#TODO: Edit the respective files to point to the new HTML file that was made