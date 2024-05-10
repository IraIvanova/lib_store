from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import Plan


class SubscriptionPlanView(View):
    def get(self, request):
        context = {
            "plans": Plan.objects.all()
        }

        return render(request, "subscription_plans_page.html", context)


class SubscriptionChangePlanView(View):
    def get(self, request, id):
        request.user.plan = Plan.objects.get(pk=id)
        request.user.save()

        messages.success(request, "Subscription plan was successfully changed!")

        return redirect("subscription_plans")
