from .models import AddToCart, Registration, ShoeList, CompanyList, CompanyBanner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serailizer import RegisterSerializer, CompanySerializer, AddToCartSerializer, ShoeSerializer, BannerSerializer
import datetime


class RegisterViewSet(APIView):

    def get_object(self, mobile):
        try:
            return Registration.objects.get(mobile=mobile)
        except Exception:
            raise Http404

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        mobile = request.data["mobile"]
        snippet = self.get_object(mobile)
        serializer = RegisterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateViewSet(APIView):

    def post(self, request):
        try:
            mobile = request.data["mobile"]
            password = request.data["password"]
            Registration.objects.get(mobile=mobile, password=password)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CompanyDetailViewSet(APIView):

    def get(self,request):
        try:
            response = []
            data = CompanyList.objects.all()
            for d in data:
                response.append(CompanySerializer(d).data)
            payload = dict(company=response)
            return Response(payload, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ShoesViewSet(APIView):

    def post(self, request):
        try:
            company = request.data['company']
            response = []
            shoes = ShoeList.objects.filter(company__id=company)
            company = CompanyList.objects.get(id=company)
            banner = CompanyBanner.objects.get(name=company.company_name)
            for d in shoes:
                response.append(ShoeSerializer(d).data)
            payload = dict(shoes=response, banner=BannerSerializer(banner).data)

            return Response(payload, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddToCartViewSet(APIView):
    def get_object(self, id):
        try:
            return AddToCart.objects.get(id=id)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            response = []
            id = request.GET['id']
            user = Registration.objects.get(id=id)
            cart = AddToCart.objects.filter(user=user, status=True)
            for d in cart:
                response.append(ShoeSerializer(d.shoe).data)
            payload = dict(shoes = response)
            return Response(payload, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            user_id = request.data["user"]
            shoe_id = request.data["shoe"]
            items = request.data['items']
            user = Registration.objects.get(id=user_id)
            shoes = ShoeList.objects.get(id=shoe_id)
            serializer = AddToCart(user=user, items=items, shoe=shoes, price=shoes.price * items,
                                   date=datetime.datetime.now().date())
            serializer.save()
            return Response(AddToCartSerializer(serializer).data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            id = request.data['id']
            cart = self.get_object(id)
            items = request.data.get("items", cart.items)
            cart.price = items * cart.shoe.price
            cart.items = items
            cart.date = datetime.datetime.now().date()
            cart.save()
            return Response(AddToCartSerializer(cart).data, status=status.HTTP_202_ACCEPTED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)