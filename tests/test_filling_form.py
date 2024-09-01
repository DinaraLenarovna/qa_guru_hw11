from modules.pages.registration_form_page import RegistrationPage


def test_practice_form_create_user():
    registration_form = RegistrationPage()
    registration_form.open()
    registration_form.fill_first_name("Dinara")
    registration_form.fill_last_name("Safina")
    registration_form.fill_email("dinatest@bk.ru")
    registration_form.choose_gender()
    registration_form.fill_phone_number("7999991991")
    registration_form.fill_date_of_birth("1999","April", "11")
    registration_form.fill_subjects("Maths")
    registration_form.fill_hobbies()
    registration_form.upload_picture("test_image.jpg")
    registration_form.fill_address("Russia, Ufa, Lenina St., 1")
    registration_form.select_state("Haryana")
    registration_form.select_city("Panipat")
    registration_form.submit()
    registration_form.assert_user_submitted_form(
        'Dinara Safina',
        'dinatest@bk.ru',
        'Female',
        '7999991991',
        '11 April,1999',
        'Maths',
        'Sports, Reading',
        'test_image.jpg',
        'Russia, Ufa, Lenina St., 1',
        'Haryana Panipat')

