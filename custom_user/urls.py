from django.urls import path
from .views import SubscriptionPlanView, SubscriptionChangePlanView

urlpatterns = [
    path('plans/', SubscriptionPlanView.as_view(), name='subscription_plans'),
    path('plans/change/<int:id>', SubscriptionChangePlanView.as_view(), name='change_plan'),
]
