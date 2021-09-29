from rest_framework import serializers
from mainapp.hostel.hostelModel import Room, Hostel, RoomAllotment
from django.http import JsonResponse

"""Hostel Serializer"""
class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

"""Room SERIALIZER"""
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


"""Room Allotment SERIALIZER"""
class RoomAllotmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAllotment
        fields = [
            'student',
            'room',
            'alloted'
        ]
    #Overide create method toupdate the room status vacant to false
    def create(self, validated_data):
        student = validated_data.pop('student')
        room = validated_data.pop('room')
        room_obj = Room.objects.get(room_id = room.room_id)
        alotted_room = validated_data.pop('alloted')
        try:
            room_allotment = RoomAllotment.objects.create(student=student, room=room, alloted=alotted_room)
            room_allotment.save()
            room_obj.update(vacant = False)
            return room_allotment
        except:
            return JsonResponse({"Error": "Something went wrong"})


