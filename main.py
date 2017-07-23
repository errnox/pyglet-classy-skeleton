import random
import pyglet

class App(object):
  def __init__(self, window):
    self.window = window
    self.main_label = pyglet.text.Label(
      'Hello', font_name='Monospace', x = self.window.width//2,
      y=self.window.height//2, anchor_x='center', anchor_y='center')
    self.colors = [
      (255, 0, 0, 255),
      (0, 255, 0, 255),
      (0, 0, 255, 255),
      (255, 255, 0, 255),
      (255, 255, 0, 255),
    ]

  def update(self):
    self.main_label.color = random.choice(self.colors)
    self.main_label.x += 1
    if self.main_label.x > self.window.width:
      self.main_label.x = 0
    elif self.main_label.x < 0:
      self.main_label.x = self.window.width


if __name__ == '__main__':
  window = pyglet.window.Window(width=800, height=600)

  app = App(window)

  @window.event
  def on_draw():
    window.clear()
    app.update()
    app.main_label.draw()

  @window.event
  def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
      app.main_label.x = self.width / 2
    elif symbol == pyglet.window.key.LEFT:
      app.main_label.x -= 10
    elif symbol == pyglet.window.key.RIGHT:
      app.main_label.x += 10

  pyglet.app.run()
