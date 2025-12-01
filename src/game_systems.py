"""
Sistema de gestión de dinero, gacha y personajes
"""
import random
from config import GACHA_CHARACTERS, LUCKY_BLOCK_COST


class PlayerWallet:
    """Gestiona el dinero del jugador y conversión a dinero del juego"""
    
    def __init__(self, initial_money=20.0):
        self.gacha_money = initial_money  # Dinero USD/del juego
        self.spent_on_gacha = 0.0
        self.inventory = []  # Personajes coleccionados
        self.daily_earnings = {}  # {day: amount}
    
    def add_daily_salary(self, day, amount):
        """Registra el salario del día"""
        self.daily_earnings[day] = amount
    
    def can_afford_lucky_block(self):
        """Verifica si puede comprar un Lucky Block"""
        return self.gacha_money >= LUCKY_BLOCK_COST
    
    def spend_on_gacha(self, amount):
        """Gasta dinero en gacha"""
        if self.gacha_money >= amount:
            self.gacha_money -= amount
            self.spent_on_gacha += amount
            return True
        return False
    
    def convert_salary_to_gacha(self, day, amount):
        """Convierte salario de un día a dinero del juego"""
        if day in self.daily_earnings:
            self.gacha_money += amount
            return True
        return False
    
    def add_character(self, character):
        """Añade un personaje al inventario"""
        self.inventory.append(character)
    
    def get_total_spent_on_gacha(self):
        """Retorna el total gastado en gacha"""
        return self.spent_on_gacha


class GachaSystem:
    """Sistema de Lucky Blocks y personajes gacha"""
    
    def __init__(self):
        self.characters = GACHA_CHARACTERS
    
    def pull_lucky_block(self, count=1):
        """Realiza un pull de Lucky Block(s) basado en pesos"""
        results = []
        for _ in range(count):
            weights = [char["weight"] for char in self.characters]
            character = random.choices(self.characters, weights=weights, k=1)[0]
            results.append(character.copy())
        return results
    
    def get_all_characters(self):
        """Retorna lista de todos los personajes posibles"""
        return self.characters.copy()


class PlayerInventory:
    """Gestiona el inventario de personajes del jugador"""
    
    def __init__(self):
        self.characters = []  # Lista de personajes adquiridos
    
    def add_character(self, character):
        """Añade un personaje al inventario"""
        self.characters.append(character)
    
    def get_characters_by_rarity(self, rarity):
        """Filtra personajes por rareza"""
        return [char for char in self.characters if char["rarity"] == rarity]
    
    def get_character_count(self):
        """Cuenta total de personajes"""
        return len(self.characters)
    
    def get_unique_characters(self):
        """Retorna personajes únicos (sin duplicados)"""
        unique = {}
        for char in self.characters:
            if char["name"] not in unique:
                unique[char["name"]] = 0
            unique[char["name"]] += 1
        return unique
