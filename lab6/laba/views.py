from django.shortcuts import redirect

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from laba.models import Customer
from laba.permission import IsAdminOrReadOnly
from laba.serializer import CustomerSerializer


# Create your views here.
class CustomerAPIList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CustomerAPIGet(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = Customer.objects.all()
    template_name = 'laba/get_customer.html'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response({'serializer': serializer,'customer': customer})


class CustomerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'laba/customer_list.html'
    serializer_class = CustomerSerializer
    def get(self, request):
        queryset = Customer.objects.all()
        return Response({'customers': queryset})

class CustomerChange(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'laba/customer_detail.html'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response({'serializer': serializer, 'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'customer': customer})
        serializer.save()
        return redirect('customer-list')
