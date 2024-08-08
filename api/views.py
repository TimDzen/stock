from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import ApiUser, Product, Stock, Business
from api.permissions import IsProviderOrReadOnly, IsCustumerOrReadOnly
from api.serializers import UserSerializer, StockSerializer, ProductSerializer, BusinessSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class StockModelViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления экземплярами Product.
    Предоставляет метод 'GET' для получения экземпляров Product, отфильтрованных по текущему пользователю.
    Права доступа:
        - IsProviderOrReadOnly: Только поставщики могут изменять, другие могут только просматривать.
    """
    permission_classes = (IsProviderOrReadOnly,)
    queryset = Product.objects.none()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user.id)


class BusinessModelViewSet(viewsets.ModelViewSet):
     """
    ViewSet для управления экземплярами Business.
    Предоставляет операции CRUD для экземпляров Business, отфильтрованных по текущему пользователю.
    Права доступа:
        - IsCustumerOrReadOnly: Только клиенты могут создавать или обновлять, другие могут только просматривать.
    """
    permission_classes = (IsCustumerOrReadOnly,)
    queryset = Business.objects.none()
    serializer_class = BusinessSerializer

    def create(self, request, *args, **kwargs):
         """
        Обрабатывает создание экземпляра Business.
        Проверяет, что запрашиваемое количество продукта доступно на складе
        перед созданием экземпляра Business и обновлением количества продукта.
         """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.validated_data.get('product')
        quantity = serializer.validated_data.get('quantity')
        product = get_object_or_404(Product, id=product_id.id)
        if product.quantity < quantity:
            return Response(
                {'error': 'Запрошенное количество товара превышает имеющееся на складе'},
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_create(serializer)
        product.quantity -= quantity
        product.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user.id)
