# app/urls.py
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet

router = routers.SimpleRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

convo_router = routers.NestedSimpleRouter(router, r'conversations', lookup='conversation')
convo_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = router.urls + convo_router.urls
