from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404

from .models import Topic, Description, Reply, Comment

# Create your views here.
# The relationships between models are: Topic is the parent class to Description and Reply. Reply is the parent class to
# Comment. All the classes take Topic as a foreign key field and Comment also takes Reply as a foreign key field. Topic
# is described as title in the UI. Reply is described as comment in the UI. Comment is described as reply in the UI.


def menu(request):
    """The starting menu page for LegalQA"""
    return render(request, 'legal_qa/menu.html')


@login_required
def topics(request):
    """The topics list page of LegalQA"""
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'legal_qa/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    descriptions = topic.description_set.order_by('date_added')
    replies = topic.reply_set.order_by('-date_added')
    user = request.user
    context = {'topic': topic, 'descriptions': descriptions, 'replies': replies, 'user': user}
    return render(request, 'legal_qa/topic.html', context)


@login_required
def new_question(request):
    """Add a new topic."""
    if request.POST.get('new_topic') and request.POST.get('new_description'):
        # POST data submitted; process data.
        new_topic = Topic()
        new_topic.text = request.POST.get('new_topic')
        new_topic.owner = request.user
        new_topic.save()
        new_description = Description()
        new_description.text = request.POST.get('new_description')
        new_description.topic = new_topic
        new_description.owner = request.user
        new_description.save()
        return redirect('legal_qa:topics')

    # Display a blank input.
    return render(request, 'legal_qa/new_question.html')


@login_required
def edit_topic(request, topic_id):
    """Edit an existing topic."""
    topic = Topic.objects.get(id=topic_id)
    descriptions = topic.description_set.order_by('date_added')
    replies = topic.reply_set.order_by('-date_added')
    user = request.user

    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # POST data submitted; process data.
        topic.text = request.POST.get('edit_topic')
        topic.save()
        return redirect('legal_qa:topic', topic_id=topic_id)

    # Display an input with original text.
    context = {'topic': topic, 'descriptions': descriptions, 'replies': replies, 'user': user}
    return render(request, 'legal_qa/topic.html', context)


@login_required
def edit_description(request, description_id):
    """Edit an existing description."""
    description = Description.objects.get(id=description_id)
    topic = description.topic
    descriptions = topic.description_set.order_by('date_added')
    replies = topic.reply_set.order_by('-date_added')
    user = request.user

    if topic.owner != request.user:
        raise Http404

    if request.POST.get('edit_description'):
        # POST data submitted; process data.
        description.text = request.POST.get('edit_description')
        description.save()
        return redirect('legal_qa:topic', topic_id=topic.id)

    # Display an input with original text.
    context = {'topic': topic, 'descriptions': descriptions, 'replies': replies, 'user': user}
    return render(request, 'legal_qa/topic.html', context)


@login_required
def new_reply(request, topic_id):
    """Add a new reply for a particular legal question."""
    topic = Topic.objects.get(id=topic_id)
    descriptions = topic.description_set.order_by('date_added')
    replies = topic.reply_set.order_by('-date_added')
    user = request.user

    if request.POST.get('new_reply'):
        # POST data submitted; process data.
        new_reply = Reply()
        new_reply.text = request.POST.get('new_reply')
        new_reply.topic = topic
        new_reply.owner = request.user
        new_reply.save()
        return redirect('legal_qa:topic', topic_id=topic_id)

    context = {'topic': topic, 'descriptions': descriptions, 'replies': replies, 'user': user}
    return render(request, 'legal_qa/topic.html', context)


@login_required
def new_comment(request, reply_id):
    """Add a new comment for a particular reply."""
    reply = Reply.objects.get(id=reply_id)
    topic = reply.topic

    if request.POST.get('new_comment'):
        # POST data submitted; process data.
        new_comment = Comment()
        new_comment.text = request.POST.get('new_comment')
        new_comment.topic = topic
        new_comment.reply = reply
        new_comment.owner = request.user
        new_comment.save()
        return redirect('legal_qa:topic', topic_id=topic.id)

    # Display a blank input.
    context = {'topic': topic, 'reply': reply}
    return render(request, 'legal_qa/new_comment.html', context)


@login_required
def new_comment_from_comment(request, comment_id):
    """Add a new comment for a particular reply clicked from the button on a comment"""
    comment = Comment.objects.get(id=comment_id)
    reply = comment.reply
    topic = reply.topic

    if request.POST.get('new_comment'):
        # POST data submitted; process data.
        new_comment = Comment()
        new_comment.text = request.POST.get('new_comment')
        new_comment.topic = topic
        new_comment.reply = reply
        new_comment.owner = request.user
        new_comment.save()
        return redirect('legal_qa:topic', topic_id=topic.id)

    # Display a blank input.
    context = {'topic': topic, 'comment': comment}
    return render(request, 'legal_qa/new_comment_from_comment.html', context)

