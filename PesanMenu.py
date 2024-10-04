menu = {
    '1': ('Nasi Goreng', 15000),
    '2': ('Ayam Bakar', 20000),
    '3': ('Mie Goreng', 12000),
    '4': ('Sate Ayam', 25000),
    '5': ('Es Teh', 5000),
    '6': ('Es Jeruk', 7000)
}

def index():
    return render_template('menu.html', menu=menu)
def order():
    order_items = []
    total_price = 0

    for key, (item, price) in menu.items():
        quantity = int(request.form.get(f'quantity_{key}', 0))
        if quantity > 0:
            order_items.append((item, quantity, price * quantity))
            total_price += price * quantity

    return render_template('order.html', order_items=order_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
