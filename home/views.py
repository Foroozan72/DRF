# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from .models import Person , Answer , Question
from .serializers import PersonSerializer , QuestionSerializer ,AnswerSerializer
from  rest_framework.permissions import IsAuthenticated , AllowAny
from  rest_framework import status
from  permissions import IsOwnerOrReadOnly
from  rest_framework.throttling import UserRateThrottle , AnonRateThrottle


class Home(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self , request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons , many = True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    throttle_classes =[UserRateThrottle , AnonRateThrottle]


    #     'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ], alternative in setting , just for this view

    def get(self , request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions , many=True)
        return  Response(srz_data.data , status=status.HTTP_200_OK)
    

class CreateQuestionView(APIView):
    """
        CREATE A NEW QUESTION 

    """
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self , request):
        srz_data=QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data , status=status.HTTP_200_OK)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    

class UpdateQuestionView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self , request , pk):
        questions = Question.objects.get(id=pk)
        self.check_object_permissions(request, questions)
        srz_data = QuestionSerializer(instance=questions , data=request.data , partial =True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_200_OK)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)


class DeleteQuestionView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self , request , pk):
        questions = Question.objects.get(id=pk)
        questions.delete()
        return Response({'message' : 'questions is deleted'} , status=status.HTTP_200_OK)



# class Home(APIView):
#     def get(self,request):
#         esm=request.query_params['name'] ##به ما یک دیکشنری میده 
#         return Response({'first_name':esm})
    
#     def post(self,request):
#         esme_shakhs=request.data['name']
#         # print(esme_shakhs)
#         return Response({'first_name':esme_shakhs})



# @api_view((['GET', 'POST' , 'PUT']))
# def Home(request):
#     return Response({"message": "Hello, world!"})



# class Home(View):
#     def get(self , request):
#         return render(request , 'home/index.html')

# Create your views here.
