from eCommerce.models import Product

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
            total_price = product.price * quantity  # Calculate total price for the product
            cart_items.append({
                'product_id': product.id,
                'product': product,
                'quantity': quantity,
                'price': product.price,
                'total_price': total_price,  # Include the calculated total price in the cart item
                'image_url': product.image.url,
            })

        return cart_items
    
    def get_qty(self):
        quantities = self.cart
        return quantities
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
