def add_product(name, price, quantity):
    product = {'name': name, 'price': price, 'qty': quantity}
    products.append(product)
    print(f"Đã thêm sản phẩm: {product}")

# Cập nhật trong main()
if choice == '1':
    name = input("Nhập tên sản phẩm: ")
    price = int(input("Nhập giá sản phẩm: "))
    qty = int(input("Nhập số lượng tồn kho: "))
    add_product(name, price, qty)

