#   -Code mã hoá tin nhắn văn bản
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Tạo cặp khóa RSA (khóa công khai và khóa riêng tư)
key = RSA.generate(2048)

# Lưu khóa riêng tư vào file "private.pem"
private_key = key.export_key()
with open("private.pem", "wb") as f:
    f.write(private_key)

# Lưu khóa công khai vào file "public.pem"
public_key = key.publickey().export_key()
with open("public.pem", "wb") as f:
    f.write(public_key)

# Mã hóa tin nhắn hoặc file văn bản
def encrypt_message(message, public_key_file):
    # Đọc khóa công khai từ file
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    # Sử dụng khóa công khai để mã hóa tin nhắn
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Giải mã tin nhắn hoặc file văn bản
def decrypt_message(encrypted_message, private_key_file):
    # Đọc khóa riêng tư từ file
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())

    # Sử dụng khóa riêng tư để giải mã tin nhắn
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()





# code mã hoá file
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Tạo cặp khóa RSA (khóa công khai và khóa riêng tư)
key = RSA.generate(2048)

# Lưu khóa riêng tư vào file "private.pem"
private_key = key.export_key()
with open("private.pem", "wb") as f:
    f.write(private_key)

# Lưu khóa công khai vào file "public.pem"
public_key = key.publickey().export_key()
with open("public.pem", "wb") as f:
    f.write(public_key)

# Mã hóa một phần của tin nhắn bằng khóa công khai
def encrypt_part(part, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_part = cipher.encrypt(part.encode())
    return base64.b64encode(encrypted_part)

# Giải mã một phần của tin nhắn bằng khóa riêng tư
def decrypt_part(part, private_key):
    part = base64.b64decode(part)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_part = cipher.decrypt(part)
    return decrypted_part.decode()

# Chia thông điệp thành các phần nhỏ hơn và mã hóa mỗi phần riêng lẻ
chunk_size = 20  # kích thước tối đa cho một phần khi mã hóa RSA với khóa 2048-bit
# test.txt tên file chứa thông điệp cần mã hóa
with open("test.txt", "r") as f:
    message = f.read()
parts = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]
public_key = RSA.import_key(open("public.pem").read())
encrypted_parts = [encrypt_part(part, public_key) for part in parts]

# Lưu các phần mã hóa vào tệp
with open("test_encrypted.txt", "wb") as f:
    for part in encrypted_parts:
        f.write(part)
        f.write(b"\n")  # để phân biệt giữa các phần

# Giải mã các phần và kết hợp chúng để tạo ra thông điệp ban đầu
encrypted_parts = []
with open("test_encrypted.txt", "rb") as f:
    for line in f:
        line = line.strip()
        if line:
            encrypted_parts.append(line)
private_key = RSA.import_key(open("private.pem").read())
decrypted_parts = [decrypt_part(part, private_key) for part in encrypted_parts]
decrypted_message = "".join(decrypted_parts)

# Lưu thông điệp được giải mã vào tệp
with open("test_decrypted.txt", "w") as f:
    f.write(decrypted_message)
