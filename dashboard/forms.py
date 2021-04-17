from django.forms import ModelForm, DateInput
from .models import lecture_update, pending_assignment, upcoming_test, important_information
from bootstrap_datepicker_plus import DateTimePickerInput


class Date_Input(DateInput):
    input_type = 'datetime-local'

    
class lecture_updateAdd (ModelForm):
    class Meta:
        model = lecture_update
        fields = [
            "course_name", "course_code", "venue", "time_start", "time_end", "course_topic", "lecture_requirement", "attendance",
        ]
        widgets = {'time_start': Date_Input(), 'time_end': Date_Input() }


class Add_pending_assignment (ModelForm):
    class Meta:
        model = pending_assignment
        fields = [
            "course_name", "assignment_question",  "submitted_to_who", "where_to_submit", "assignment_marks", "assignment_dueDate",
        ]
        widgets = {'assignment_dueDate': Date_Input() }
        


class Add_upcoming_test (ModelForm):
    class Meta:
        model = upcoming_test
        fields = [
            "course_name", "date_announced", "test_time", "venue", "area_of_concentration", "test_marks",
        ]
        widgets = {'test_time': Date_Input(), 'date_announced': Date_Input() }


class Add_important_information (ModelForm):
    class Meta:
        model = important_information
        fields = [
            "title", "body",
        ]
        