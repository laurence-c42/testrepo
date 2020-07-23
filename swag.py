import pygame, sys
from pygame.locals import *

class banner:
    def __init__(self, screen, colour, bordercolour, xpos, ypos, width, height, borderwidth, text, textcolour, textfont, textsize):
        #Draw box
        self.box = pygame.draw.rect(screen, colour, Rect((xpos, ypos), (width, height)))
        #Draw border
        self.border = pygame.draw.rect(screen, bordercolour, Rect((xpos, ypos), (width, height)), borderwidth)
        #Create text
        self.text = pygame.font.SysFont(textfont, textsize).render(text, 1, textcolour)
        #Get text size
        textwidth = self.text.get_size()[0]
        textheight = self.text.get_size()[1]
        #Shrink text if necessary
        if textwidth > width * 0.95:
            textsize *= width * 0.95 / textwidth
            self.text = pygame.font.SysFont(textfont, int(textsize)).render(text, 1, textcolour)
            textwidth = self.text.get_size()[0]
            textheight = self.text.get_size()[1]
        if textheight > height * 0.95:
            textsize *= height * 0.95 / textheight
            self.text = pygame.font.SysFont(textfont, int(textsize)).render(text, 1, textcolour)
            textwidth = self.text.get_size()[0]
            textheight = self.text.get_size()[1]
        #Get text position
        textxpos = xpos + (width - textwidth) / 2
        textypos = ypos + (height - textheight) / 2
        #Create text
        screen.blit(self.text, (textxpos, textypos))

class button:
    def __init__(self, screen, colour, hovercolour, bordercolour, xpos, ypos, width, height, borderwidth, text, textcolour, textfont, textsize, mouseposition):
        #Define variables for use later
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        #Create box, with colour dependant on whether the cursor is within the box limits
        if pygame.Rect(xpos, ypos, width, height).collidepoint(mouseposition):
            self.box = pygame.draw.rect(screen, hovercolour, Rect((xpos, ypos), (width, height)))
        else:
            self.box = pygame.draw.rect(screen, colour, Rect((xpos, ypos), (width, height)))
        #Create border
        self.border = pygame.draw.rect(screen, bordercolour, Rect((xpos, ypos), (width, height)), borderwidth)
        #Create text
        self.text = pygame.font.SysFont(textfont, textsize).render(text, 1, textcolour)
        #Get text size
        textwidth = self.text.get_size()[0]
        textheight = self.text.get_size()[1]
        #Shrink text if necessary
        if textwidth > width * 0.95:
            textsize *= width * 0.95 / textwidth
            self.text = pygame.font.SysFont(textfont, int(textsize)).render(text, 1, textcolour)
            textwidth = self.text.get_size()[0]
            textheight = self.text.get_size()[1]
        if textheight > height * 0.95:
            textsize *= height * 0.95 / textheight
            self.text = pygame.font.SysFont(textfont, int(textsize)).render(text, 1, textcolour)
            textwidth = self.text.get_size()[0]
            textheight = self.text.get_size()[1]
        #Get text position
        textxpos = xpos + (width - self.text.get_size()[0]) / 2
        textypos = ypos + (height - self.text.get_size()[1]) / 2
        #Create text
        screen.blit(self.text, (textxpos, textypos))

    def pressed(self, mouseposition, clicked):
        #Returns True if button has been clicked
        return clicked and event.type == pygame.MOUSEBUTTONUP and pygame.Rect(self.xpos, self.ypos, self.width, self.height).collidepoint(mouseposition)
