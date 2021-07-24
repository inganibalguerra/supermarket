from user_ms.models.user_model import User
from user_ms.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import JsonResponse

class UserList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Login(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, user,password):

        # user = "anibal"
        # password= "guerra"

        # user = self.request.params.get('user')
        # password= self.request.params.get('password')


        queryset = User.objects.filter(user=(user),password=(password))

        serializer = UserSerializer(instance=queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

        # return JsonResponse(data)