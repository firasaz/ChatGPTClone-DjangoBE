from django.urls import path
from .views import handshake, users_list
from chat.views import chats_list, create_new_chat
from chatmessages.views import messages_list, create_message

urlpatterns = [
    path("handshake/", handshake),
    path("users/", users_list),
    
    path('chat/chat-list/', chats_list),
    path('chat/new-chat/', create_new_chat),
    
    path('messages/messages-list/', messages_list),
    path('messages/new-message/', create_message),
    ]
