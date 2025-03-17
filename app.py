#tipicamente questo file si chiama main

import flet as ft

from controller import Controller
from view import View

def main(page: ft.Page):
    v = View(page) #diciamo alla view qual è la pagina che modifica #crea la view
    c = Controller(v) # creo Controller e passo la view
    v.setController(c) # passo alla view il controller
    v.loadInterface() #creo il collegamento tra view e controller

ft.app(target=main)
