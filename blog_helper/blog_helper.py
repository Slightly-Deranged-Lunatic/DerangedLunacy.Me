import os
from pathlib import Path
import file_funcs
import html
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

    file_funcs.make_paths(dates)
    standardize_working_directory()
    file_funcs.create_files(dates)
    standardize_working_directory()

def standardize_working_directory():
    # Makes the working directory /html/subpages/my_blog no matter where the script is being ran from.
    # This way we can use relative paths.
    website_directory = os.path.dirname(__file__)
    os.chdir(website_directory)
    os.chdir(f"{Path.cwd().parent}/html/subpages/my_blog")

if __name__ == "__main__":
    main()

#TODO: Edit the respective files to point to the new HTML file that was made