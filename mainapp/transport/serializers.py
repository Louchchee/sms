from rest_framework import serializers
from mainapp.transport.transportModel import transport , SchoolBus, busReservation
from django.http import JsonResponse
from rest_framework.validators import UniqueValidator

"""TRANSPORT SERIALIZER"""
class TransPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = transport
        fields = '__all__'


class busSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBus
        fields = '__all__'
    

class busReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = busReservation
        fields = '__all__'

    def create(self, validated_data):
      
        reservation_id = validated_data.pop('reservation_id')
        student = validated_data.pop('student')
        bus = validated_data.pop('bus')
        status = validated_data.pop('status')
        try:
            reservation = busReservation.objects.create(reservation_id=reservation_id, student=student, status=status, bus=bus)
            
            if reservation.status == 'Active':
                seats = bus.seats_available - 1
                bus.seats_available = seats
                bus.save()
                reservation.save()
            return reservation
                
        except:
            return False

    def update(self,instance,validated_data):
        
        obj = busReservation.objects.get(id=instance.id)
        val_status = validated_data.get('status')
        
        if obj.status == "Active" and val_status == "Inactive":
            bus = validated_data.get('bus')
            seats = bus.seats_available + 1
            bus.seats_available = seats
            bus.save()

        if obj.status == "Inactive" and val_status == "Active":
            bus = validated_data.get('bus')
            seats = bus.seats_available - 1
            bus.seats_available = seats
            bus.save()
        instance.reservation_id = validated_data.get('reservation_id', instance.reservation_id)
        instance.status = validated_data.get('status', instance.status)
        instance.student = validated_data.get('student', instance.student)
        instance.bus = validated_data.get('bus', instance.bus)
        instance.save()
        return instance



