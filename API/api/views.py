from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import *
from ..models import *
from rest_framework.views import APIView
from rest_framework.status import *



##These are using generic ListaPi and other model classes

    #Users
class CreateUser(ListCreateAPIView):
    queryset = User.objects.all()
    permission_class = AllowAny
    serializer_class = createcustomer

class SingleUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_class = AllowAny
    serializer_class = createcustomer


    #Category
class CreateCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    permission_class = AllowAny
    serializer_class = createcategory

class SingleCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_class = AllowAny
    serializer_class = createcategory

    #Subcategory

class CreateSubCategory(ListCreateAPIView):
        queryset = SubCategory.objects.all()
        permission_class = AllowAny
        serializer_class = createsubcategory

class SingleSubCategory(RetrieveUpdateDestroyAPIView):
        queryset = SubCategory.objects.all()
        permission_class = AllowAny
        serializer_class = createsubcategory


    #Product
class createProduct(ListCreateAPIView):
        queryset = Product.objects.all()
        permission_class = AllowAny
        serializer_class = createproductform

class SingleProduct(RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        permission_class = AllowAny
        serializer_class = createproductform


    #Add_Cart
class createAddCart(ListCreateAPIView):
        queryset = Add_card.objects.all()
        permission_class = AllowAny
        serializer_class = createorderform

class SingleAddCart(RetrieveUpdateDestroyAPIView):
        queryset = Add_card.objects.all()
        permission_class = AllowAny
        serializer_class = createorderform



    #Dilvery Order Details
class createOrder(ListCreateAPIView):
        queryset = DeliveryOrder.objects.all()
        permission_class = AllowAny
        serializer_class = dilveryform

class SingleOrder(RetrieveUpdateDestroyAPIView):
        queryset = DeliveryOrder.objects.all()
        permission_class = AllowAny
        serializer_class = dilveryform

    #Payment Order Details
class createPayment(ListCreateAPIView):
        queryset = Payment.objects.all()
        permission_class = AllowAny
        serializer_class = PaymentForm


class LoginApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message':'login successfully','data':serializer.data},status=HTTP_200_OK)
        return Response({'message':'the code is not wroking'},status=HTTP_400_BAD_REQUEST)



'''
class UpdateUser(UpdateAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer


class DeleteUser(DestroyAPIView):
    queryset = SignUp.objects.all()
    permission_class = AllowAny
    serializer_class = SignUpSerializer
    '''