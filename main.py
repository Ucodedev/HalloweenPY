import pygame

# Initialisation de Pygame
pygame.init()

# Création d'une fenêtre vide (nous n'allons pas l'afficher)
screen = pygame.display.set_mode((400, 400))

# Chargement des sons
cri_sound = pygame.mixer.Sound('cri.mp3')
fantome_sound = pygame.mixer.Sound('fantome.mp3')
sorciere_sound = pygame.mixer.Sound('sorciere.mp3')
zombie_sound = pygame.mixer.Sound('zombie.mp3')

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cri_sound.play()
            elif event.key == pygame.K_UP:
                fantome_sound.play()
            elif event.key == pygame.K_RIGHT:
                sorciere_sound.play()
            elif event.key == pygame.K_LEFT:
                zombie_sound.play()

