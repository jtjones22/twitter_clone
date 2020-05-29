from django.shortcuts import render

from notification.models import Notification

# Create your views here.


def notification_view(request):
    html = 'notification.html'
    alerts = Notification.objects.filter(reciever=request.user.id)
    num_of_alerts = []
    for alert in alerts:
        if alert.read is False:
            num_of_alerts.append(alert)
    context = {'alerts': alerts}
    response = render(request, html, context)
    for alert in alerts:
        if alert.read is False:
            alert.read = True
            alert.save()
    return response
