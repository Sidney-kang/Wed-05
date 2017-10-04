# Created by : Sidney Kang
# Created on : 4 Oct. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_05
# This scene

from scene import * 
import ui

class MainGameScene(Scene):
      def setup(self):
          #Add Mt blue background colour
          self.background = SpriteNode(position = self.size/2, 
                                       color = ('black'), 
                                       parent = self,
                                       size = self.size)

          spaceship_position = self.size/2
          spaceship_position.y = spaceship_position.y - 280                                             
          self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                      parent = self,
                                      position = spaceship_position)
