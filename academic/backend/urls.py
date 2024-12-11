
# from django.urls import path
# from .views import register_user, LoginView, ProfileView
# from django.urls import path
# from .views import (
#     StudentListCreateView, StudentDetailView, StaffListCreateView, StaffDetailView,
#     TeacherListCreateView, TeacherDetailView, ClassListCreateView, ClassDetailView,
#     SubjectListCreateView, SubjectDetailView, ResponsibilityListCreateView, ResponsibilityDetailView,
#     AddressListCreateView, AddressDetailView, AttendanceListCreateView, AttendanceDetailView,
#     GradeListCreateView, GradeDetailView, DisciplineListCreateView, DisciplineDetailView,
#     TimetableListCreateView, TimetableDetailView, TransportListCreateView, TransportDetailView,
#     LibraryListCreateView, LibraryDetailView, MessageListCreateView, MessageDetailView,
#     NoticeboardListCreateView, NoticeboardDetailView,UserDetailView
# )

# urlpatterns = [
#     path('api/v1/users/', UserDetailView.as_view(), name='user-list'),
#     path('api/v1/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # For individual user operations
#     path('api/v1/register/', register_user, name='register_user'),
#     path('api/v1/login/', LoginView.as_view(), name='login'),
#     path('api/v1/profile/', ProfileView.as_view(), name='profile'),

#     path('api/v1/students/', StudentListCreateView.as_view(), name='student-list'),
#     path('api/v1/students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
#     path('api/v1/staff/', StaffListCreateView.as_view(), name='staff-list'),
#     path('api/v1/staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
#     path('api/v1/teachers/', TeacherListCreateView.as_view(), name='teacher-list'),
#     path('api/v1/teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
#     path('api/v1/classes/', ClassListCreateView.as_view(), name='class-list'),
#     path('api/v1/classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
#     path('api/v1/subjects/', SubjectListCreateView.as_view(), name='subject-list'),
#     path('api/v1/subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
#     path('api/v1/responsibilities/', ResponsibilityListCreateView.as_view(), name='responsibility-list'),
#     path('api/v1/responsibilities/<int:pk>/', ResponsibilityDetailView.as_view(), name='responsibility-detail'),
#     path('api/v1/addresses/', AddressListCreateView.as_view(), name='address-list'),
#     path('api/v1/addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
#     path('api/v1/attendance/', AttendanceListCreateView.as_view(), name='attendance-list'),
#     path('api/v1/attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
#     path('api/v1/grades/', GradeListCreateView.as_view(), name='grade-list'),
#     path('api/v1/grades/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),
#     path('api/v1/discipline/', DisciplineListCreateView.as_view(), name='discipline-list'),
#     path('api/v1/discipline/<int:pk>/', DisciplineDetailView.as_view(), name='discipline-detail'),
#     path('api/v1/timetable/', TimetableListCreateView.as_view(), name='timetable-list'),
#     path('api/v1/timetable/<int:pk>/', TimetableDetailView.as_view(), name='timetable-detail'),
#     path('api/v1/transport/', TransportListCreateView.as_view(), name='transport-list'),
#     path('api/v1/transport/<int:pk>/', TransportDetailView.as_view(), name='transport-detail'),
#     path('api/v1/library/', LibraryListCreateView.as_view(), name='library-list'),
#     path('api/v1/library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
#     path('api/v1/messages/', MessageListCreateView.as_view(), name='message-list'),
#     path('api/v1/messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
#     path('api/v1/noticeboard/', NoticeboardListCreateView.as_view(), name='noticeboard-list'),
#     path('api/v1/noticeboard/<int:pk>/', NoticeboardDetailView.as_view(), name='noticeboard-detail'),
# ]

# updated using ROUTE
from rest_framework_simplejwt import views as jwt_views
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ForgotPasswordRequestView, ResetPasswordView, register_user, LoginView,
    UserViewSet, StudentViewSet, TeacherViewSet, DepartmentViewSet, CourseViewSet,
    EnrollmentViewSet, ClassroomViewSet, ScheduleViewSet, GradeViewSet,
    AttendanceViewSet, ParentViewSet, AnnouncementViewSet, FeeViewSet
)

# Define the router
router = DefaultRouter()

# Register viewsets with the router
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'fees', FeeViewSet)

# Add the custom views (register, login, forgot-password, reset-password) here
urlpatterns = [
    path('forgot-password/', ForgotPasswordRequestView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),
    path('register/', register_user, name='register_user'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('index/', views.HomeView.as_view(), name ='index'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
]

# Add the router URLs
urlpatterns += router.urls

