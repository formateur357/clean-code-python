#######################################################################""
# Exemple de base

def a(a: int, b: int) -> int :
    return a * b

def calcul_aire_rectangle(longueur: int, largeur: int) -> int :
    return longueur * largeur

#######################################################################""

# Principe SOLID

#######################################################################""

# S -> SRP : Single Responsibility Principle
# ❌ Mauvais : la classe fait trop de choses (persistance + envoi de mails)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self):
        # logique de persistence
        print(f"Enregistrement de {self.name} dans la base...")

    def send_mail(self, message):
        # logique d'envoi de mail
        print(f"Envoi de '{message}' à {self.email}...")

        # ✅ Bon : séparation des responsabilités

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    def save(self, user: User):
        print(f"Enregistrement de {user.name} dans la base...")


class EmailService:
    def send(self, user: User, message: str):
        print(f"Envoi de '{message}' à {user.email}...")

#######################################################################""

# O : Open/Closed Principle

# ❌ Mauvais
def calculer_prix(mode, montant):
    if mode == "paypal": ...
    elif mode == "cb": ...

# ✅ Bon
class Paiement:
    def calculer(self, montant): pass

class Paypal(Paiement): ...
class CarteBancaire(Paiement): ...

#######################################################################""
 # P : Liskov substitution principle

 # ❌ Mauvais
class Bird:
    def fly(self):
        return "je vole dans le ciel !"

class Penguin(Bird):
    def fly(self):
        raise Exception("je ne peux pas voler !")
    
def make_it_fly(bird: Bird):
    print(bird.fly)

make_it_fly(Bird()) ✅ Bon

make_it_fly(Penguin()) ❌ Erreur "viole le principe de substitus4tion de Liskov"

from abc import ABC, abstractmethod

# ✅ Bon
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return self.fly()
    
    def fly(self):
        return "je vole dans le ciel."
    
class WalkingBird(Bird):
    def move(self):
        return self.walk()
    
    def walk(self):
        return "je marche sur la terre."
    
class Sparrow(FlyingBird):
    pass

class Penguin(WalkingBird):
    pass

def make_it_move(bird: Bird):
    print(bird.move())

make_it_move(Sparrow())
make_it_move(Penguin())

#######################################################################""
# Principe DIP : Dependency Inversion Principle

# Probleme couplage trop fort, on ne peut pas remplacer email par sms.

class EmailService:
    def send(self, message):
        print(f"Email envoyé : {message}")

class NotificationService():
    def __init__(self):
        self.email_service = EmailService()
    
    def notifier(self, message: str):
        self.email_service.send(message)

# Refactorisation

# from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailService(MessageService):
    def send(self, message: str):
        print(f"Email envoyé : {message}")

class SMSService(MessageService):
    def send(self, message: str):
        print(f"SMS envoyé : {message}")

class NotificationService():
    def __init__(self, service: MessageService):
        self.service = service()
    
    def notifier(self, message: str):
        self.service.send(message)