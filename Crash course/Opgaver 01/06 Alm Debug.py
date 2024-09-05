school = 'Aalborg University'
class_name = "Programering for matematikere"
number_of_lectures = 12
minutes_per_lecture = 130


total_minutes = number_of_lectures * minutes_per_lecture
total_hours = total_minutes // 60  
remaining_minutes = total_minutes % 60  


print(f"The class {class_name} is held at {school} over {number_of_lectures} lectures for a total of {total_hours} hours and {remaining_minutes} minutes.")
