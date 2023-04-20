# This form takes in the comment from a post
# Life cycle of submitting a form:
#   - When a user visits a page containing a form, they send a GET request to the server. 
#     In this case, there’s no data entered in the form, so we just want to render 
#     the form and display it.
#   - When a user enters information and clicks the Submit button, a POST request, 
#     containing the data submitted with the form, is sent to the server. At 
#     this point, the data must be processed, and two things can happen:
#       - The form is valid, and the user is redirected to the next page.
#       - The form is invalid, and empty form is once again displayed. The user is 
#         back at step 1, and the process repeats.
from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )