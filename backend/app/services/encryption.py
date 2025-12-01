from cryptography.fernet import Fernet
from app.core.config import settings
import base64
import hashlib


class EncryptionService:
    """
    Handles encryption/decryption of sensitive data (SSN, insurance, payment info).
    Uses Fernet (symmetric encryption) for tokenization.
    """
    
    def __init__(self):
        # Derive a valid Fernet key from the encryption key in settings
        key = self._derive_key(settings.ENCRYPTION_KEY)
        self.cipher = Fernet(key)
    
    def _derive_key(self, password: str) -> bytes:
        """
        Derive a valid 32-byte Fernet key from any password string.
        """
        # Use SHA256 to create a consistent 32-byte key
        key = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(key)
    
    def encrypt(self, data: str) -> str:
        """
        Encrypt sensitive data and return a token.
        
        Args:
            data: Plain text data (e.g., SSN, credit card)
        
        Returns:
            Encrypted token string
        """
        if not data:
            return None
        
        encrypted_bytes = self.cipher.encrypt(data.encode())
        return encrypted_bytes.decode()
    
    def decrypt(self, token: str) -> str:
        """
        Decrypt a token back to original data.
        
        Args:
            token: Encrypted token string
        
        Returns:
            Original plain text data
        """
        if not token:
            return None
        
        decrypted_bytes = self.cipher.decrypt(token.encode())
        return decrypted_bytes.decode()
    
    def tokenize_ssn(self, ssn: str) -> str:
        """Tokenize Social Security Number"""
        return self.encrypt(ssn)
    
    def detokenize_ssn(self, token: str) -> str:
        """Detokenize SSN"""
        return self.decrypt(token)
    
    def tokenize_card(self, card_number: str) -> str:
        """Tokenize credit card number"""
        return self.encrypt(card_number)
    
    def detokenize_card(self, token: str) -> str:
        """Detokenize credit card"""
        return self.decrypt(token)
    
    def tokenize_insurance(self, insurance_number: str) -> str:
        """Tokenize insurance number"""
        return self.encrypt(insurance_number)
    
    def detokenize_insurance(self, token: str) -> str:
        """Detokenize insurance number"""
        return self.decrypt(token)
    
    def mask_ssn(self, ssn: str) -> str:
        """
        Mask SSN for display (XXX-XX-1234)
        """
        if not ssn or len(ssn) < 4:
            return "XXX-XX-XXXX"
        return f"XXX-XX-{ssn[-4:]}"
    
    def mask_card(self, card_number: str) -> str:
        """
        Mask credit card for display (****-****-****-1234)
        """
        if not card_number or len(card_number) < 4:
            return "****-****-****-****"
        return f"****-****-****-{card_number[-4:]}"


# Singleton instance
encryption_service = EncryptionService()