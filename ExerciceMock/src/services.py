import re
from .user import User

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class UserService:
    def __init__(self, repo, notifier, logger):
        self.repo = repo
        self.notifier = notifier
        self.logger = logger

    def register(self, email: str) -> User:
        if not EMAIL_REGEX.match(email or ""):
            self.logger.error(f"Invalid email : {email!r}")
            raise(ValueError("Invalide Email"))

        user = User(email=email, is_active=True)
        saved = self.repo.save(user)
        self.notifier.send(email, "Welcome !", "Bienvenue sur la plateforme !")
        self.logger.info(f"User registered : {saved.email}")

        return saved

    def reset_password(self, email: str) -> str:
        user = self.repo.get_by_email(email)

        if user is None:
            self.logger.error(f"User not found : {email}")
            raise(LookupError("User not found"))
        
        token = "reset123"
        user.reset_token = token
        self.repo.save(user)
        self.notifier.send(email, "Password reset", f"Votre token : {user.reset_token}")
        self.logger.info(f"Password reset for: {email}")
        
        return token