from email import message
from django.shortcuts import redirect, render
from apps.cart.cart import Cart
from apps.core.forms import ContactForm, FeedbackForm
from apps.core.models import Contact, Feedback

from apps.product.models import Product


def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    # cart = Cart(request)
    return render(request, 'core/frontpage.html', {'newest_products': newest_products})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            vendor = Contact.objects.create(
                name=contact.name, email=contact.email, message=contact.message)

            return redirect('frontpage')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save()

            vendor = Feedback.objects.create(
                name=feedback.name, feedback=feedback.feedback)

            return redirect('frontpage')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback.html',{'form':form})
