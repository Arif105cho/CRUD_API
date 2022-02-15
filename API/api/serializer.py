from rest_framework.serializers import *

from ..models import Add_card, Product, User, Category,DeliveryOrder,SubCategory,Payment

from ..models import User

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER




class createcustomer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class createorderform(ModelSerializer):
    class Meta:
        model = Add_card
        fields = "__all__"


class createproductform(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class createcategory(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class createsubcategory(ModelSerializer):
    class Meta:
        model=SubCategory
        fields='__all__'



class dilveryform(ModelSerializer):
    class Meta:
        model = DeliveryOrder
        fields = '__all__'

class PaymentForm(ModelSerializer):
    class Meta:
        model=Payment
        fields = '__all__'


class LoginSerializer(Serializer):
    email=EmailField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(error_messages={'required':'password key is required','blank':'password is required'})
    token=CharField(read_only=True,required=False)

    def validate(self,data):
        qs=User.objects.filter(email=data.get('email'))
        if not qs.exists():
            raise ValidationError("No account with this email")

        user=qs.first()
        if user.check_password(data.get('password'))==False:
            raise ValidationError("Invalid Password")
        payload =  jwt_payload_handler(user)
        token   =  jwt_encode_handler(payload)
        data['token'] ='JWT '+str(token)
        return data
