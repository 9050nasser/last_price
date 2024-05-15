
import frappe

@frappe.whitelist()
def get_selling_price(customer, item):
    x = frappe.get_all("Customer Price", filters={"customer": customer, "item": item}, fields="price", order_by="date")
    return x