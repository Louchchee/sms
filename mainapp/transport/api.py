from rest_framework.viewsets import ModelViewSet
from mainapp.transport.transportModel import transport, SchoolBus, busReservation
from mainapp.transport.serializers import TransPortSerializer, busSerializer, busReservationSerializer


"""Transport API for CRUD operations"""
class TransportViewSet(ModelViewSet):
    serializer_class = TransPortSerializer
    queryset = transport.objects.all()


class BusViewSet(ModelViewSet):
    serializer_class =  busSerializer
    queryset = SchoolBus.objects.all()

class ReservationViewSet(ModelViewSet):
    serializer_class = busReservationSerializer
    queryset = busReservation.objects.all()