import zlib
from cryptography.fernet import Fernet

# Configuration: Set your Master Key and the Webhook payload
MASTER_KEY = "YOUR_MASTER_KEY_HERE"
ENCRYPTED_PAYLOAD = """YOUR_ENCRYPTED_DATA_HERE"""

def decrypt_payload():
    try:
        # Initialize Fernet with the master key
        f = Fernet(MASTER_KEY.encode())
        
        # Decrypt the AES-256 payload
        encrypted_bytes = ENCRYPTED_PAYLOAD.strip().encode()
        decrypted_compressed = f.decrypt(encrypted_bytes)
        
        # Decompress zlib data and decode to string
        original_text = zlib.decompress(decrypted_compressed).decode('utf-8')
        
        print("\n" + "═"*50)
        print("✅ DECRYPTION SUCCESSFUL")
        print("═"*50)
        print(original_text)
        print("═"*50)
        
    except Exception as e:
        print("\n" + "!"*50)
        print(f"❌ ERROR: {e}")
        print("!"*50)
        print("Tip: Verify that the MASTER_KEY is correct.")
        print("Tip: Make sure the ENCRYPTED_PAYLOAD was copied in full.")

if __name__ == "__main__":
    decrypt_payload()
