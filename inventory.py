## canh bao nhap hang
def check_low_stock():
    low_stock_items = [p for p in products if p['qty'] < 5]
    if not low_stock_items:
        print("Không có sản phẩm sắp hết hàng.")
        return
    print("\n===== CẢNH BÁO HẾT HÀNG =====")
    for product in low_stock_items:
        print(f"{product['name']} - Số lượng: {product['qty']}")






