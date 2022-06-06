#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    '''API View test'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''retornar lista de caracteristicas del api view'''
        an_apiview=[
            'Usamos metodos http como funciones (get, post, patch, put, delete)',
            'es similar a una vista tradicional de django',
            'nos da mayor control sobre la logica de nuestra app',
            'esta mapeado manualmente a los urls',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})


    def post(self, request):
        '''Crea un  msj con nuestro nombre'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Actualizar un objeto'''
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        '''Actualización parcial de un objeto'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        ''' Eliminar un objeto '''
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    def list(self,request):
        '''retornar lista'''
        a_viewset = [
            'Usa acciones list, create, retrieve, update, partial_update',
            'automaticamente mapea a los urls usando routers',
            'provee mas funcionalidad con menos codigo'
        ]

        return Response({'message':'Hola','a_viewset':a_viewset})
    
    def create(self, request):
        '''crear msj hola mundo con viewset'''

        serializer_class = serializers.HelloSerializer

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        '''obtiene un objeto y su Id'''
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        '''Actualizar un objeto'''
        return Response({'method':'PUT'})
    
    def partial_update(self, request, pk=None):
        '''Actualización parcial de un objeto'''
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        ''' Eliminar un objeto '''
        return Response({'method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    ''' Crear y actualizar perfiles '''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # agregamos clase de autenticacion
    permission_classes = (permissions.UpdateOwnProfile,) # agregamos clase con permiso creado 