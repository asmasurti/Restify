from rest_framework.generics import ListAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from .models import Rating
from property.models import Property
from accounts.models import RestifyUser
from reservation.models import Reservation
from .serializers import RatingSerializer 

from django.contrib.contenttypes.models import ContentType

from rest_framework.pagination import PageNumberPagination


# Pagination for all Comment lists
class RatingResultsSetPagination(PageNumberPagination):
    # Default
    page_size = 10
    # Name of the query parameter for controlling page_size
    page_size_query_param = 'page_size'
    max_page_size = 20


class ViewRatingsForProperty(ListAPIView):
    serializer_class = RatingSerializer
    pagination_class = RatingResultsSetPagination

    def get_queryset(self):
        property = get_object_or_404(Property, id=self.kwargs["property_id"])
        content_type_obj = ContentType.objects.get_for_model(property)

        ratings = Rating.objects.filter(receiver_type=content_type_obj,
                                        receiver_id=property.id)
        return ratings
    

class ViewRatingsForGuest(ListAPIView):
    serializer_class = RatingSerializer
    pagination_class = RatingResultsSetPagination

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(RestifyUser, id=self.kwargs["user_id"])
        self.check_if_was_guest(user)

        content_type_obj = ContentType.objects.get_for_model(user)

        ratings = Rating.objects.filter(receiver_type=content_type_obj,
                                        receiver_id=user.id)
        return ratings
    
    def check_if_was_guest(self, user):
        # Check if <user> has/ has had reservation on current user's properties.
        this_user = self.request.user
        stays_with_user = Reservation.objects.filter(property__owner=this_user,
                                                     guest=user)
        if not stays_with_user.exists():
            raise ValidationError(
                {'Unauthorized':
                 'This guest has not stayed at your properties before.'})

        return None
    

class RateProperty(CreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    permission_classes = [IsAuthenticated]

    receiver_type = Property


class RateUser(CreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    permission_classes = [IsAuthenticated]

    receiver_type = RestifyUser