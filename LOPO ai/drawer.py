import time
import pygame
import image_handler
import sys


class drawer():
    def __init__(self, r):
        self.res = r
        self.Subject = 0

        self.windowRes = [1024, 1024]
        self.pixelres = [self.windowRes[0] /
                         self.res[0], self.windowRes[1]/self.res[1]]

        self.gridDisplay = pygame.display.set_mode(
            (self.windowRes[0], self.windowRes[1]))
        pygame.display.get_surface().fill((0, 0, 0))

        self.pixels = []

        self.Intensity = [[0.25, 0.5, 0.25],
                          [0.5, 1, 0.5],
                          [0.25, 0.5, 0.25]]
        self.IntensityCoords = [[[-1, -1], [0, -1], [1, -1]],
                                [[-1, 0], [0, 0], [1, 0]],
                                [[-1, 1], [0, 1], [1, 1]]]
        for i in range(self.res[0]):
            self.pixels.append([])
            for x in range(self.res[1]):
                self.pixels[i].append(0)
        self.holdingMouse = False
        self.lastPixel = []
        self.image_handler = image_handler.imageHandler()

    def current_milli_time(self):
        return round(time.time() * 1000)

    def match_event_key(self, key):
        match key:
            case pygame.K_0:
                self.Subject = 0
            case pygame.K_1:
                self.Subject = 1
            case pygame.K_2:
                self.Subject = 2
            case pygame.K_3:
                self.Subject = 3
            case pygame.K_4:
                self.Subject = 4
            case pygame.K_5:
                self.Subject = 5
            case pygame.K_6:
                self.Subject = 6
            case pygame.K_7:
                self.Subject = 7
            case pygame.K_8:
                self.Subject = 8
            case pygame.K_9:
                self.Subject = 9

    def start_drawing_train(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.holdingMouse = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.holdingMouse = False
                elif event.type == pygame.KEYDOWN:
                    self.match_event_key(event.key)
                    match event.key:
                        case pygame.K_DELETE:
                            self.gridDisplay.fill((0, 0, 0))
                            self.pixels = []
                            for i in range(self.res[0]):
                                self.pixels.append([])
                                for x in range(self.res[1]):
                                    self.pixels[i].append(0)
                        case pygame.K_END:
                            self.gridDisplay.fill((0, 0, 0))
                            filedir = "Opas ai\data\d"+str(self.Subject) + "\img-" + \
                                str(self.current_milli_time())+".png"
                            open(filedir, "w").close()
                            self.image_handler.write_image(
                                filedir, self.pixels, (self.res[0], self.res[1]), 270, True)
                            self.pixels = []
                            for i in range(self.res[0]):
                                self.pixels.append([])
                                for x in range(self.res[1]):
                                    self.pixels[i].append(0)

            if self.holdingMouse:
                mouse = pygame.mouse.get_pos()
                x, y = round(mouse[0]/self.pixelres[0]-self.pixelres[0] / (8*self.res[0])
                             ), round(mouse[1]/self.pixelres[1]-self.pixelres[1]/(8*self.res[1]))
                if self.lastPixel == [x, y]:
                    continue
                self.lastPixel = [x, y]
                pygame.draw.rect(self.gridDisplay, (255, 255, 255), [
                    x*self.pixelres[0], y*self.pixelres[1], self.pixelres[0], self.pixelres[1]])
                for y2 in range(3):
                    for x2 in range(3):
                        color = round(255*self.Intensity[y2][x2])
                        self.IntensityCoord = self.IntensityCoords[y2][x2]
                        xp, yp = x + \
                            self.IntensityCoord[0], y+self.IntensityCoord[1]

                        self.pixels[xp][yp] += color
                        color = self.pixels[xp][yp]
                        if color > 255:
                            color = 255
                            self.pixels[xp][yp] = 255
                        pygame.draw.rect(self.gridDisplay, (color, color, color), [
                            x*(self.pixelres[0])+self.IntensityCoord[0]*self.pixelres[0], y*(self.pixelres[1])+self.IntensityCoord[1]*self.pixelres[1], self.pixelres[0], self.pixelres[1]])

            pygame.display.update()

    def start_drawing_free(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.holdingMouse = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.holdingMouse = False
                elif event.type == pygame.KEYDOWN:
                    self.match_event_key(event.key)
                    match event.key:
                        case pygame.K_DELETE:
                            self.gridDisplay.fill((0, 0, 0))
                            self.pixels = []
                            for i in range(self.res[0]):
                                self.pixels.append([])
                                for x in range(self.res[1]):
                                    self.pixels[i].append(0)
                        case pygame.K_END:
                            self.gridDisplay.fill((0, 0, 0))
                            filedir = "Opas ai\data\d"+str(self.Subject) + "\img-" + \
                                str(self.current_milli_time())+".png"
                            open(filedir, "w").close()
                            self.image_handler.write_image(
                                filedir, self.pixels, (self.res[0], self.res[1]), 270, True)
                            self.pixels = []
                            for i in range(self.res[0]):
                                self.pixels.append([])
                                for x in range(self.res[1]):
                                    self.pixels[i].append(0)

            if self.holdingMouse:
                mouse = pygame.mouse.get_pos()
                x, y = round(mouse[0]/self.pixelres[0]-self.pixelres[0] / (8*self.res[0])
                             ), round(mouse[1]/self.pixelres[1]-self.pixelres[1]/(8*self.res[1]))
                if self.lastPixel == [x, y]:
                    continue
                self.lastPixel = [x, y]
                pygame.draw.rect(self.gridDisplay, (255, 255, 255), [
                    x*self.pixelres[0], y*self.pixelres[1], self.pixelres[0], self.pixelres[1]])
                for y2 in range(3):
                    for x2 in range(3):
                        color = round(255*self.Intensity[y2][x2])
                        self.IntensityCoord = self.IntensityCoords[y2][x2]
                        xp, yp = x + \
                            self.IntensityCoord[0], y+self.IntensityCoord[1]

                        self.pixels[xp][yp] += color
                        color = self.pixels[xp][yp]
                        if color > 255:
                            color = 255
                            self.pixels[xp][yp] = 255
                        pygame.draw.rect(self.gridDisplay, (color, color, color), [
                            x*(self.pixelres[0])+self.IntensityCoord[0]*self.pixelres[0], y*(self.pixelres[1])+self.IntensityCoord[1]*self.pixelres[1], self.pixelres[0], self.pixelres[1]])

            pygame.display.update()


a = drawer([32, 32])
drawer.start_drawing_free(a)
