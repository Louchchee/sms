from mainapp.models import CustomUser, ProfileImage, SessionYear, Manager
from django.contrib import admin
from mainapp.parents.parentsModel import parent
from mainapp.students.studentModel import student, enroll

from mainapp.transport.transportModel import transport
from mainapp.teacher.teacherModel import teacher
from mainapp.classRoom.classesSubjects import classRoom, Subject
from mainapp.attendence.attendenceModel import ClassRoutine, StudentAttendance
from mainapp.payment.paymentModel import invoice, payment, invoice_category
from mainapp.examination.examModel import Exam, StudentAppearedExam, mark, StudentResult
from . models import Notice

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    display_fields = ('user.id')

@admin.register(parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('parent_id','customuser', 'phone', 'address', 'profession')

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'customuser','birthday', 'phone')

# @admin.register(dormitory)
# class DormitoryAdmin(admin.ModelAdmin):
#     list_display = ('dormitory_id', 'name', 'number_of_room', 'description')

@admin.register(transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('transport_id', 'route_name', 'number_of_vehicle', 'route_fare')

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'sex')

@admin.register(classRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    display_fields = '__all__'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','class_id', 'teacher')


admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    display_fields = '__all__'

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    display_fields = '__all__'

admin.site.register(ProfileImage)
admin.site.register(StudentResult)
admin.site.register(SessionYear)
admin.site.register(ClassRoutine)
admin.site.register(enroll)
admin.site.register(mark)
admin.site.register(Exam)
admin.site.register(StudentAppearedExam)
admin.site.register(invoice)
admin.site.register(payment)
admin.site.register(invoice_category)

admin.site.register(Notice)