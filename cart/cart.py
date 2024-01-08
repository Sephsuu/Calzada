from eCommerce.models import Product
from cart.models import Order

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart        

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_product(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart_items = []
        for product in products:
            quantity = self.cart[str(product.id)]
            total_price = product.price * quantity 
            cart_items.append({
                'product_id': product.id,
                'product': product,
                'quantity': quantity,
                'price': product.price,
                'total_price': total_price, 
                'image_url': product.image.url,
            })

        print(cart_items)

        return cart_items
    
    def get_qty(self):
        quantities = self.cart
        return quantities
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
    def checkout(self, customer):
        products = self.get_product()
        total_amount = 0
        
        # Calculate total amount for the order
        for item in products:
            total_amount += item['total_price']

        # Create an order and transfer items
        order = Order.objects.create(
            customer=customer,
            total_amount=total_amount,
            # Add other fields here as needed
        )
        for item in products:
            order.products.add(item['product'])
        
        self.cart = {}
        self.session['session_key'] = {} 
        self.session.modified = True

    def delete_all_orders(self):
        Order.objects.all().delete()