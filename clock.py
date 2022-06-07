# imports
from datetime import datetime
import pygame

pygame.init()

# icon
icon = pygame.image.load('icon/digitalClock.png')
pygame.display.set_icon(icon)

# display
display = pygame.display.set_mode((450, 200))
pygame.display.set_caption('Digital Clock')
clock = pygame.time.Clock()

# fonts
larger_font = pygame.font.Font('font/DS-DIGI.TTF', 130)
medium_font = pygame.font.Font('font/DS-DIGI.TTF', 40)
smaller_font = pygame.font.Font('font/DS-DIGI.TTF', 35)
FPS = 60

# colors
black = (0,0,0)
green = (57,255,20)
red =  (255,0,40)

# main color
color = green

# date/month
months = ['January', 'February', 'March', 'April', 'May', 
'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

# main function
run = True
while run:
    display.fill(black)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    current = datetime.now()
    year = current.strftime("%Y")
    month = int(current.strftime('%m'))
    date = current.strftime("%d")
    today = datetime.today()
    day = today.weekday()
    day = days[day]
    month = months[month - 1]
    hour = int(current.strftime('%H'))
    minute = current.strftime('%M:%S')
    
    am = 'AM'
    if hour > 12:
        hour = hour-12
        am = 'PM'
    
    time = f'{hour}:{minute}'
    
    time_text = larger_font.render(time, True, color)
    am_text = medium_font.render(am, True, red)
    month_text = smaller_font.render(month, True, color)
    day_text = smaller_font.render(day, True, color)
    day_num = smaller_font.render(date, True, color)
    year_num = smaller_font.render(year, True, color)
   
    display.blit(time_text, (22,20))
    display.blit(am_text, (405,0))
    display.blit(month_text, (15,150))
    display.blit(day_text, (290,150))
    display.blit(day_num, (93,150))
    display.blit(year_num, (180,150))
   
    clock.tick(FPS)
    pygame.display.update()