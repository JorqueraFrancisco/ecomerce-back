from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProductSerializer, FileSerializer
from rest_framework.views import APIView
from .models import Product, File
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

class FileView(APIView):

    # permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, file_id, format=None):
        """
        Delete a specific file by id.
        """

        file = get_object_or_404(File, file_id=file_id)
        file.delete()
        return Response({"message": f"File {file_id} has been deleted successfully."})


class ProductView(APIView):

    def post(self, request, format=None):

        product_serializer = ProductSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product = product_serializer.save()

        # file_data = {
        #     'product': product.product_id,
        #     'image': request.data.get('image', 'test'),
        # }

        # file_serializer = FileSerializer(data=file_data)
        # file_serializer.is_valid(raise_exception=True)
        # file_serializer.save()

        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, product_id=None, format=None):
        if product_id:
            product = Product.objects.get(pk=product_id)
            serializer = ProductSerializer(product)
            response = Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            response = Response(serializer.data)

        return response

    def delete(self, request, product_id, format=None):
        """
        Delete a specific product by id.
        """

        product = get_object_or_404(Product, product_id=product_id)
        product.delete()
        return Response({"message": f"Product {product_id} has been deleted successfully."})

    def put(self, request, product_id, format=None):
        product = get_object_or_404(Product, pk=product_id)
        product_serializer = ProductSerializer(product, data=request.data)
        product_serializer.is_valid()
        product_serializer.update(product, request.data)

        return Response(product_serializer.data)

    def get_permissions(self):
        """
        Define los permisos que se aplicarán en función de la petición.
        """
        if self.request.method == 'GET':

            return []
        elif self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAdminUser()]
        else:
            return []