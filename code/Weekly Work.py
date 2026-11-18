# ============================================================================
# ## SESSION 1
# Build a window in pygame, display images and include basic animations
# ============================================================================

# ----------------------------------------------------------------------------
### Build a window in pygame
# Below I want you to set up a basic window 
# ----------------------------------------------------------------------------

#install any packages you might need below



# create the a blank window which we can run our game on 
# make sure you can close the window too



# ============================================================================
# ============================================================================
# ============================================================================
# DO NOT GO FURTHER THAN HERE, FINISHED CODE FOR THE ABOVE TASK
# IS UNDERNEATH!!!!!!!!!!!!!!
# ============================================================================
# ============================================================================
# ============================================================================











# ----------------------------------------------------------------------------
# Adding Background Images and text
# Now using the script I have provided that is commented out.
# uncomment the script and add a the sky image and ground image 
# from the graphics file to the window ensuring you place your new code in the right place
# then I want you to add text to the screen too using the font in the 'font' file 
# !!!!! make sure you comment out the script above this^^^!!!!
# ----------------------------------------------------------------------------

# pygame.init()
# screen = pygame.display.set_mode((800,400))
# pygame.display.set_caption('Runner')
# clock = pygame.time.Clock()

# #Task: - load the font style

# #Task: - load your background

# #Task: - load your font Surface qualities (what you want to say, color ect)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     #Task: - blit the background and font 

    

#     pygame.display.update()
#     clock.tick(60)



# ============================================================================
# ============================================================================
# ============================================================================
# DO NOT GO FURTHER THAN HERE, FINISHED CODE FOR THE ABOVE TASK
# IS UNDERNEATH!!!!!!!!!!!!!!
# ============================================================================
# ============================================================================
# ============================================================================











# ----------------------------------------------------------------------------
# Include Basic Animations
# Here we will add an image of a snail from our graphics file and move it from the left to the
# left to the right of the screen in a loop.
# ----------------------------------------------------------------------------

# pygame.init()
# screen = pygame.display.set_mode((800,400))
# pygame.display.set_caption('Runner')
# clock = pygame.time.Clock()

# #load the font style
# font_style = pygame.font.Font('font/Pixeltype.ttf', 50)

# #load your background
# sky_surface = pygame.image.load('graphics/Sky.png')
# ground_surface = pygame.image.load('graphics/ground.png')

# #Task: - Load in the snail image and set it's x position


# #load your font Surface qualities (what you want to say, color ect)
# font_surface = font_style.render('Game', False, 'green')

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     #blit the background and font
#     screen.blit(sky_surface, (0,0))
#     screen.blit(ground_surface,(0,300))
#     screen.blit(font_surface, (300, 50))

#     #Task: - blit in the image of the snail (remeber to make a change here to help edit the x coordinate)


#     #Task: - write a SIMPLE line of code to move the snail from the left to the right of the screen


#     #Task:- include an if statement to reset the snail to the right of the screen if it reaches the left edge



#     pygame.display.update()
#     clock.tick(60)