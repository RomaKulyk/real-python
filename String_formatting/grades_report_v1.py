student ={
    "name": "John Doe",
    "subjects":[
        {
            "name": "Mathematics",
            "grade": 88,
            "comment": "Excellent Improvement."
        },
        {
            "name": "Science",
            "grade": 92,
            "comment": "Outstanding performance."
        },
        {
            "name": "History",
            "grade": 78,
            "comment": "Needs to participate more."
        },
        {
            "name": "Art",
            "grade": 85,
            "comment": "Very creative."
        },
    ],
}

def build_student_report(student):
    # Defines a heading for the report
    report_header = f"Progress Report. Student: {student['name']}"
    # Sums all the grades
    total = sum(subject["grade"] for subject in student["subjects"])
    # Computes the average of the grades
    average = total / len(student["subjects"])
    # Expresses the average grade as a floating-poin number with two decimal 
    # places
    average_report = f"Average: {average:.2f} / 100\n"
    # Defines the first line of the subject subreport
    subject_report = "Course Details:\n"
    # Starts a loop over the subjects
    for subject in student["subjects"]:
        # Adds more information to the subject subreport
        subject_report += (
            # Aligns the name to the left within 15 characters
            f"{subject['name']: <15}"
            # Displays the grade using up to three characters
            f"Grade: {subject['grade']: 3d}"
            # Adds the comment part
            f" Comment: {subject['comment']}\n"
        )

    return( f"""
{report_header}
{average_report}
{subject_report}
Thank you for reviewing the progress report.
""")

print(build_student_report(student))
