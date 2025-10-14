import base64

def image_to_base64(filepath):
    try:
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        return ""

# Assuming your logo file is named 'university_logo.png'
logo_b64 = image_to_base64("logo.png") 

print("--- LOGO B64 ---")
print(logo_b64)