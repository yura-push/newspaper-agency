from django.test import TestCase

from agency.forms import RedactorCreationForm, RedactorExperienceUpdateForm


class FormsTests(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "Test123as",
            "password2": "Test123as",
            "first_name": "Test First",
            "last_name": "Test Last",
            "years_of_experience": 12,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_experience_update_form(self):
        form_data = {
            "years_of_experience": 14,
        }
        form = RedactorExperienceUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
