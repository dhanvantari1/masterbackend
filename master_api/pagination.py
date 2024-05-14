from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class CustomPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "message": getattr(self, "custom_message", ""),
                "status": getattr(self, "custom_status", status.HTTP_200_OK),
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "count": self.page.paginator.count,
                "data": data,
            }
        )