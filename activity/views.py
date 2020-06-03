from activity.serializers import User_serialize, Activity_periods_serializers
from activity.models import User, Activity_periods
from django.http import JsonResponse


def home(request):
    members = {}
    all_user = User.objects.all()
    user = User_serialize(all_user, many=True)
    user_data = user.data
    if user_data:
        members['ok'] = True
        members['members'] = user.data
    return JsonResponse(members)