from rest_framework import generics
from .models import Component
from .serializers import ComponentSerializer

# create components list api

class ComponentListAPI(generics.ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = []

# create component detail api

class ComponentDetailAPI(generics.RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = []
    lookup_field = 'pk'


# create component create api

class ComponentCreateAPI(generics.CreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = []

# create component update api

class ComponentUpdateAPI(generics.UpdateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = []
    lookup_field = 'pk'


# create component delete api

class ComponentDeleteAPI(generics.DestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = []
    lookup_field = 'pk'


# create component search api

class ComponentSearchAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

# create component filter api

class ComponentFilterAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        filter_term = self.request.GET.get('filter', None)
        if filter_term:
            queryset = queryset.filter(category=filter_term)
        return queryset

# create component sort api

class ComponentSortAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        sort_term = self.request.GET.get('sort', None)
        if sort_term:
            queryset = queryset.order_by(sort_term)
        return queryset

# create component pagination api

class ComponentPaginationAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Component.objects.all()
        page_number = self.request.GET.get('page', 1)
        return queryset.paginate(page=page_number, per_page=10)

# create component recommendation api

class ComponentRecommendationAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        recommendations = component.recommended_component.all()
        return
        recommendations

# create component sale api

class ComponentSaleAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        sales = component.sale_component.all()
        return sales
    
# create component wishlist api

class ComponentWishlistAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        wishlists = component.wishlist_component.all()
        return wishlists


# create component build list api

class ComponentBuildListAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        build_lists = component.build_list_component.all()
        return build_lists


# create component build api

class ComponentBuildAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        build_id = self.kwargs.get('build_pk')
        component = Component.objects.get(pk=component_id)
        build = component.build_component.get(pk=build_id)
        return build.component_set.all()


# create component build create api

class ComponentBuildCreateAPI(generics.CreateAPIView):
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        component_id = self.kwargs.get('pk')
        build_id = self.kwargs.get('build_pk')
        component = Component.objects.get(pk=component_id)
        build = Component.objects.get(pk=build_id)
        serializer.save(component=component, build=build)


# create component build update api

class ComponentBuildUpdateAPI(generics.UpdateAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        build_id = self.kwargs.get('build_pk')
        component = Component.objects.get(pk=component_id)
        build = Component.objects.get(pk=build_id)
        return build.component_set.all()

    def perform_update(self, serializer):
        component_id = self.kwargs.get('pk')
        build_id = self.kwargs.get('build_pk')
        component = Component.objects.get(pk=component_id)
        build = Component.objects.get(pk=build_id)
        serializer.save(component=component, build=build)


# create component build delete api

class ComponentBuildDeleteAPI(generics.DestroyAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        build_id = self.kwargs.get('build_pk')
        component = Component.objects.get(pk=component_id)
        build = Component.objects.get(pk=build_id)
        return build.component_set.all()


# create component build list create api

class ComponentBuildListCreateAPI(generics.CreateAPIView):
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)


# create component build list update api

class ComponentBuildListUpdateAPI(generics.UpdateAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.build_list_component.all()


    def perform_update(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)

    
# create component build list delete api

class ComponentBuildListDeleteAPI(generics.DestroyAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.build_list_component.all()


# create component recommendation create api

class ComponentRecommendationCreateAPI(generics.CreateAPIView):
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        component_id = self.kwargs.get('pk')
        recommended_component_id = self.kwargs.get('recommended_pk')
        component = Component.objects.get(pk=component_id)
        recommended_component = Component.objects.get(pk=recommended_component_id)
        serializer.save(component=component, recommended_component=recommended_component)


# create component recommendation delete api

class ComponentRecommendationDeleteAPI(generics.DestroyAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        recommended_component_id = self.kwargs.get('recommended_pk')
        component = Component.objects.get(pk=component_id)
        recommended_component = Component.objects.get(pk=recommended_component_id)
        return component.recommended_component.all()


# create component sale create api

class ComponentSaleCreateAPI(generics.CreateAPIView):
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)


# create component sale update api

class ComponentSaleUpdateAPI(generics.UpdateAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.sale_component.all()


    def perform_update(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)


        
# create component sale delete api

class ComponentSaleDeleteAPI(generics.DestroyAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.sale_component.all()


# create component wishlist create api

class ComponentWishlistCreateAPI(generics.CreateAPIView):
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)


# create component wishlist update api

class ComponentWishlistUpdateAPI(generics.UpdateAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.wishlist_component.all()


    def perform_update(self, serializer):
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        serializer.save(component=component)


# create component wishlist delete api

class ComponentWishlistDeleteAPI(generics.DestroyAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.wishlist_component.all()


# Compatibility checker

class CompatibilityCheckerAPI(generics.ListAPIView):
    serializer_class = CompatibilitySerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        component_id = self.kwargs.get('pk')
        component = Component.objects.get(pk=component_id)
        return component.compatibility.all()


# Add Filters for price, brand, compatibility and more

class ComponentFilterAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'compatibility']
    queryset = Component.objects.all()
    permission_classes = []

    def get_queryset(self):
        queryset = Component.objects.all()
        filter_term = self.request.GET.get('filter', None)
        if filter_term:
            queryset = queryset.filter(category=filter_term)
        return queryset

# Add Search for name, brand, category and more

class ComponentSearchAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'brand', 'category']
    queryset = Component.objects.all()
    permission_classes = []
    
    def get_queryset(self): 
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

# Add Sorting for price, brand, category and more

class ComponentSortAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    queryset = Component.objects.all()
    permission_classes = []
    
    def get_queryset(self): 
        queryset = Component.objects.all()
        sort_term = self.request.GET.get('sort', None)
        if sort_term:
            queryset = queryset.order_by(sort_term)
        return queryset

# Add Pagination for 10 items per page

class ComponentPaginationAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    queryset = Component.objects.all()
    permission_classes = []
    pagination_class = PageNumberPagination
    page_size = 10
    def get_queryset(self):
        queryset = Component.objects.all()
        page_number = self.request.GET.get('page', 1)
        return queryset.paginate(page=page_number, per_page=10)


# Add Authentication for all APIs   

class ComponentAuthenticationAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    
    def get_queryset(self):

        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

# Add Authorization for all APIs

class ComponentAuthorizationAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset
        

# Add Permissions for all APIs

class IsComponentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class ComponentPermissionAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

# Add Throttling for all APIs

class ComponentThrottlingAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    throttle_classes = [UserRateThrottle]
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset


# Add Caching for all APIs

class ComponentCachingAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    cache_timeout = 60
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset


# Add Rate Limiting for all APIs

class ComponentRateLimitAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    rate_limit_classes = [UserRateThrottle]
    rate_limit_scope = 'components'
    rate_limit_message = "Too many requests, please try again later."
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset


# Add Logging for all APIs

class ComponentLoggingAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    logger = logging.getLogger(__name__)
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        self.logger.info("API accessed by user: %s", self.request.user)
        return queryset


# Add Monitoring for all APIs

class ComponentMonitoringAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    monitor = Monitor()
    
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        self.monitor.record_api_access(self.request.user)
        return queryset


# Add Testing for all APIs

class ComponentTestingAPI(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsComponentOwner]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'brand', 'category']
    def get_queryset(self):
        
        queryset = Component.objects.all()
        search_term = self.request.GET.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

    def test_get_queryset(self):
        response = self.client.get('/api/components/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
        self.assertTrue('name' in response.data[0])
        self.assertTrue('brand' in response.data[0])
        self.assertTrue('price' in response.data[0])
        self.assertTrue('category' in response.data[0])
        self.assertTrue('image' in response.data[0])
        self.assertTrue('url' in response.data[0])
        self.assertTrue('description' in response.data[0])
        self.assertTrue('rating' in response.data[0])
        self.assertTrue('reviews' in response.data[0])
        self.assertTrue('stock' in response.data[0])
        self.assertTrue('release_date' in response.data[0])
        self.assertTrue('warranty' in response.data[0])
        self.assertTrue('created_at' in response.data[0])
        self.assertTrue('updated_at' in response.data[0])
        self.assertTrue('brand' in response.data[0])
        self.assertTrue('specs' in response.data[0])
        self.assertTrue('amazon_link' in response.data[0])
        response = self.client.get('/api/components/?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

# Add Deployment for all APIs
# Add CI/CD for all APIs
# Add Security for all APIs





