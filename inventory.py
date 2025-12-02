## Xem ton kho 
def view_inventory():
    if not products:
        print("Kho hàng trống.")
        return
    print("\n===== DANH SÁCH SẢN PHẨM =====")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product['name']} - Giá: {product['price']} - Số lượng: {product['qty']}")




