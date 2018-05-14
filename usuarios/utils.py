from .models import *
# Create your tests here.
def role_user(username):
    try:
        client = Client.objects.get(username=username)
        return 1
    except Client.DoesNotExist:
        pass
    try:
        consultant = Consultant.objects.get(username=username)
        return 2
    except Consultant.DoesNotExist:
        pass
    try:
        manager = Manager.objects.get(username=username)
        return 3
    except Manager.DoesNotExist:
        pass
    try:
        user = User.objects.get(username=username)
        if user.is_superuser:
            return 0
        else:
            return -1
    except User.DoesNotExist:
        return -1

