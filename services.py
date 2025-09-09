class NotificationService:
    def send(self, email, message):
        # Ici il y aurait un appel réel à un serveur SMPT
        print(f"Sending email to {email} : {message}")
        return True
    
class UserService:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier

    def register_user(self, email):
        # logiques métier
        return self.notifier.send(email, "Welcome!")