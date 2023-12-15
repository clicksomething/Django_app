#put unorganized code here. 
from django.utils import timezone
from app.models import employee, session

def create_employee_account(first_name, last_name, middle_name, gender, email, password_encryption, role):
    new_employee = employee(
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        gender=gender,
        email=email,
        password_encryption=password_encryption,
        role=role,
        last_login=timezone.now(),
        is_logged_in=False
    )
    new_employee.save()
    return new_employee

def start_employee_session(employee_instance, IP_address, device_info):
    new_session = session(
        user_id=employee_instance,
        login_time=timezone.now(),
        logout_time=timezone.now(),
        IP_address=IP_address,
        device_info=device_info
    )
    new_session.save()
    employee_instance.is_logged_in = True
    employee_instance.save()
    return new_session
