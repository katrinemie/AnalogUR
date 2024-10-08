import pygame   #Importere pygame
import math   #Importere math
import datetime   #Importere tiden


pygame.init()
screen_size = (640, 480) 
screen = pygame.display.set_mode(screen_size) #vinduestørrelse
pygame.display.set_caption("Analog_ur")  


center_position = (screen_size[0] // 2, screen_size[1] // 2)
radius = 200 #Cirkel størrelse / radius
font = pygame.font.Font(None, 36) #Skriftype 


def draw_clock(): #Definere draw_clock
    screen.fill((187, 232, 237))  #Så jeg kan få en lyserblå baggrund / skærmen bliver lyserblåp :)

    
    pygame.draw.circle(screen, (200, 200, 255), center_position, radius)  # Tegner den blå cirkel, som er selve uret
    pygame.draw.circle(screen, (255, 0, 255), center_position, radius, 3)  # tegner cirklen og farven på kanten af uret

    
    for i in range(12): #loop, kører 12 gange, timer på uret
        angle = math.radians((360 / 12) * (i + 1) - 90) #Vil gerne have timemarkinger og tal, så vinklen begrenes til de 12 timemærkninger

        inner_x = center_position[0] + (radius - 10) * math.cos(angle)
        inner_y = center_position[1] + (radius - 10) * math.sin(angle) #koordinaterne for hvor markeringerne skal starte og slutte
        outer_x = center_position[0] + radius * math.cos(angle)
        outer_y = center_position[1] + radius * math.sin(angle)

        pygame.draw.line(screen, (255, 0, 255), (int(inner_x), int(inner_y)), (int(outer_x), int(outer_y)), 3)

        
        text_x = center_position[0] + (radius - 30) * math.cos(angle) 
        text_y = center_position[1] + (radius - 30) * math.sin(angle)
        number = font.render(str(i + 1), True, (0, 0, 0))  #timetal fra 1-12
        text_rect = number.get_rect(center=(int(text_x), int(text_y)))
        screen.blit(number, text_rect) #Det her tilføjer tallene til skærmen

    
    middle_radius = 5 #bare en lille cirkel i midten af uret
    pygame.draw.circle(screen, (0, 0, 255), center_position, middle_radius)

    
    current_time = datetime.datetime.now() #Det her går ind og henter den nuværende tid, så uret passer med tiden som den er lige nu
    hour = current_time.hour % 12 #fra 24 timer format til 12 timer
    minute = current_time.minute
    second = current_time.second

    
    hour_angle = math.radians((360 / 12) * hour - 90 + (minute / 60) * 30)
    minute_angle = math.radians((360 / 60) * minute - 90) #Finder vinklerne, så det passer med uret
    second_angle = math.radians((360 / 60) * second - 90)

    
    hour_hand_length = radius * 0.5 #længde timeviser
    minute_hand_length = radius * 0.7 #længde minut
    second_hand_length = radius * 0.9 #længde sekunder

    hour_x = center_position[0] + hour_hand_length * math.cos(hour_angle)
    hour_y = center_position[1] + hour_hand_length * math.sin(hour_angle)

    minute_x = center_position[0] + minute_hand_length * math.cos(minute_angle)
    minute_y = center_position[1] + minute_hand_length * math.sin(minute_angle)

    second_x = center_position[0] + second_hand_length * math.cos(second_angle)
    second_y = center_position[1] + second_hand_length * math.sin(second_angle)

    # Tegn viserne
    pygame.draw.line(screen, (8, 58, 64), center_position, (int(hour_x), int(hour_y)), 8)  #timeviser
    pygame.draw.line(screen, (0, 0, 0), center_position, (int(minute_x), int(minute_y)), 4)  #  minutviser
    pygame.draw.line(screen, (255, 0, 0), center_position, (int(second_x), int(second_y)), 2)  # sekundviser

    pygame.display.flip()  # Opdatere skærmen


clock = pygame.time.Clock() #main loop, holder det kørende
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #aflutter
            exit()

    draw_clock()  
    clock.tick(60)  # 60 fordi den kører med 60 fps, så det passer med 60 sek osv