import requests

# --- PDQ Connect API ---
PDQ_API_URL = "https://api.pdq.com/connect/v1/devices"
PDQ_API_KEY = "YOUR_PDQ_API_KEY"

def get_pdq_devices():
    headers = {"Authorization": f"Bearer {PDQ_API_KEY}"}
    response = requests.get(PDQ_API_URL, headers=headers)
    response.raise_for_status()
    return response.json()  # Adjust parsing as needed

# --- Lenovo Warranty API ---
LENOVO_API_URL = "https://supportapi.lenovo.com/v2.5/warranty"
LENOVO_API_KEY = "YOUR_LENOVO_API_KEY"

def get_lenovo_warranty(serial_number):
    params = {
        "serial": serial_number,
        "apikey": LENOVO_API_KEY
    }
    response = requests.get(LENOVO_API_URL, params=params)
    response.raise_for_status()
    return response.json()  # Adjust parsing as needed

def main():
    devices = get_pdq_devices()
    for device in devices.get("devices", []):
        serial = device.get("serialNumber")
        if serial:
            warranty = get_lenovo_warranty(serial)
            print(f"Device: {serial}, Warranty: {warranty}")

if __name__ == "__main__":
    main()