from abc import ABC

class UserRepositoryInterface(ABC):
    def insert_user(name: str, email: str, phone: str):
        pass
    
    def edit_user(id: str, name: str, email: str, phone: str):
        pass
    
    def delete_user(id: str):
        pass
