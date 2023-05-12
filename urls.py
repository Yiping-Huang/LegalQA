"""Define the URL pattern of legal_qa"""

from django.urls import path

from . import views

app_name = 'legal_qa'
urlpatterns = [
    # starting menu page
    path('legal_qa/menu/', views.menu, name='menu'),
    # topics list page
    path('legal_qa/topics/', views.topics, name='topics'),
    # typical topic page
    path('legal_qa/topics/\u003Cint:topic_id\u003E/', views.topic, name='topic'),
    # add new question page
    path('legal_qa/new_question/', views.new_question, name='new_question'),
    # edit topic page
    path('legal_qa/edit_topic/\u003Cint:topic_id\u003E/', views.edit_topic, name='edit_topic'),
    # edit description page
    path('legal_qa/edit_description/\u003Cint:description_id\u003E/', views.edit_description, name='edit_description'),
    # new reply page
    path('legal_qa/new_reply/\u003Cint:topic_id\u003E/', views.new_reply, name='new_reply'),
    # new comment page
    path('legal_qa/new_comment/\u003Cint:reply_id\u003E/', views.new_comment, name='new_comment'),
    # new comment from comment page
    path('legal_qa/new_comment_from_comment/\u003Cint:comment_id\u003E/', views.new_comment_from_comment,
         name='new_comment_from_comment'),
]
