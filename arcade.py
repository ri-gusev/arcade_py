import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Coins"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Переменные для настройки картинок (спрайты)
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        # Настройка движения курсора
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Настройка персонажа (спрайта)
        img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Создание монет
        for _ in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Расположение монет на экране
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Добавляем монеты в список
            self.coin_list.append(coin)

    def on_draw(self):
        """ Отрисовка спрайтов на экране """
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()

        # Пишем текст на экране
        output = f"Баллы: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)
        
    def on_mouse_motion(self, x, y, dx, dy):
        """Обработка движения курсора"""
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Движения и логика игры """
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    
    


   