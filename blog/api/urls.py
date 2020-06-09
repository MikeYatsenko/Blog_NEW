from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.api import views as bv

router = DefaultRouter()
router.register(r"posts", bv.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<slug:slug>/comment/", bv.CommentCreateAPIView.as_view(), name="create-comment"),
    path("posts/<slug:slug>/comments/<int:pk>", bv.CommentRUDAPIView.as_view(), name ="comment-detail"),
    path("posts/<slug:slug>/comments/", bv.CommentListAPIView.as_view(), name="comment-list"),
    path("posts/<slug:slug>/vote/", bv.PostVoteAPIView.as_view(), name="post-vote"),
    path("comments/<slug:slug>/vote/", bv.CommentVoteAPIView.as_view(), name="comment-vote"),

]
