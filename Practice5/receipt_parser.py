import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        "products": [],
        "total_amount": "",
        "date_time": "",
        "payment_method": ""
    }

    product_pattern = re.compile(
        r'\d+\.\n(.*?)\n(?:\)?(\d+,\d+) x ([\d\s,]+)\n[\d\s,]+\nPrice\n([\d\s,]+)', 
        re.DOTALL
    )
    
    products = product_pattern.findall(content)
    for p in products:
        data["products"].append({
            "name": p[0].strip().replace('\n', ' '),
            "quantity": p[1],
            "unit_price": p[2].strip(),
            "subtotal": p[3].strip()
        })

    total_match = re.search(r'Total:\n([\d\s,]+)', content)
    if total_match:
        data["total_amount"] = total_match.group(1).strip()

    dt_match = re.search(r'Время: (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', content)
    if dt_match:
        data["date_time"] = dt_match.group(1)

    payment_match = re.search(r'(Bank card|Cash):', content)
    if payment_match:
        data["payment_method"] = "Bank Card" if "Bank card" in payment_match.group(1) else "Cash"

    return data

if __name__ == "__main__":
    result = parse_receipt('raw.txt')
    print(json.dumps(result, indent=4))