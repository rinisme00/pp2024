import gzip
import shutil
import os

def compress_files(output_file, files):
    with gzip.open(output_file, "wb") as f_out:
        for file in files:
            with open(file, "rb") as f_in:
                shutil.copyfileobj(f_in, f_out)

def decompress_file(input_file, output_dir):
    with gzip.open(input_file, "rb") as f_in:
        with open(os.path.join(output_dir, "students.txt"), "wb") as students_file:
            shutil.copyfileobj(f_in, students_file)
        with open(os.path.join(output_dir, "courses.txt"), "wb") as courses_file:
            shutil.copyfileobj(f_in, courses_file)
        with open(os.path.join(output_dir, "marks.txt"), "wb") as marks_file:
            shutil.copyfileobj(f_in, marks_file)

def check_and_load_data():
    if os.path.exists("students.dat"):
        decompress_file("students.dat", ".")
