from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps


class DuplicateEntryCheckView(APIView):
    # Create your views here.
    def post(self, request):
        model_name = request.data.get("model_name")
        field_name = request.data.get("field_name")
        field_value = request.data.get("field_value")


        if model_name and field_name and field_value:
            model = apps.get_model("master_api", model_name)
            filter_kwargs = {field_name: field_value}
            if model.objects.filter(**filter_kwargs).exists():
                return Response({"status": 400, "message": f"{field_name} is already exists."}, status=400)

        return Response({"status": 200, "message": "Object does not exist."}, status=200)